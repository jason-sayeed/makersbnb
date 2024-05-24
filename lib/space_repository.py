from lib.space import *
import pandas as pd


class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection

    def add(self, space):
        rows = self._connection.execute(
            'INSERT into spaces(description, price, user_id, name, fromdate, todate, free_dates) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id', [space.description, space.price, space.user_id, space.name, space.fromdate, space.todate, space.free_dates]
        )
        space.id = rows[0]['id']
        return None

    def all(self):
        rows = self._connection.execute(
            'SELECT * FROM spaces'
        )
        spaces = []
        print(rows)
        for row in rows:
            item = Space(row['id'], row['description'], row['price'], row['user_id'], row['name'], row['fromdate'], row['todate'], row['free_dates'])
            spaces.append(item)
        return spaces

    def comprehend_freedates(self,id):
        freedate_list = self._connection.execute(
            'SELECT id, free_dates FROM spaces;'
        )
        return freedate_list

    def filter(self,fromdate,todate=0):
    # # The todate parameter has a default value of 0, meaning if it's not provided, it will be 0.
        if todate == 0:
            todate = fromdate
            # If todate is 0, then todate is assigned the value of fromdate.
        id_list = self._connection.execute(
            'SELECT id FROM spaces',
        )
        id_and_dates = {}
        for item in id_list:
            id_value = next(iter(item.values()))
            # Retrieves the first value from the current item and assigns it to id_value.
            dates_list = next(iter(self.comprehend_freedates(*item.values())))
            # Calls self.comprehend_freedates() with all values from the current item, then retrieves the first value from the returned dictionary and assigns it to dates_list.
            dates_list = (next(iter(dates_list.values())))
            # Retrieves the first value from dates_list and assigns it back to dates_list.
            while "" in dates_list:
                dates_list.remove("")
            id_and_dates.update({id_value:dates_list})
            # Updates the id_and_dates dictionary with the new key-value pair.
            
        space_ids = []
        for key, dates_list in id_and_dates.items():
        # Iterates through each key-value pair in id_and_dates.
            if all(date in dates_list for date in (fromdate, todate)):
            # Checks if both fromdate and todate are present in dates_list.
                space_ids.append(key)
                # Appends the key to space_ids if both fromdate and todate are found in dates_list.
        return space_ids
    
    def find(self, space_id):
        row = self._connection.execute(
            'SELECT * FROM spaces WHERE id = %s', [space_id]
        )
        item = Space(row['id'], row['description'], row['price'], row['name'], row['fromdate'], row['todate'])
        return item
    
    
    def remove_date(self,id,fromdate,todate=0):
        if todate == 0:
            todate = fromdate
        dates_list = self.comprehend_freedates(id)
        dates_list = (next(iter(dates_list[0].values())))
        if "{" in dates_list:
            dates_list = dates_list.replace("{","").replace("}","")
            dates_list = dates_list.split(",")
        if "[" in dates_list:
            dates_list = dates_list.replace("[","").replace("]","")
            dates_list = dates_list.split(",")
        dates_booked = []
        convertfrom = pd.to_datetime(fromdate, dayfirst=True).date()
        convertto = pd.to_datetime(todate, dayfirst=True).date()
        dates_booked = pd.date_range(start=convertfrom,end=convertto)
        dates_booked = list(dates_booked.strftime('%d-%m-%Y'))
        for date in dates_booked:
            if date in dates_list:
                dates_list.remove(date)
        self._connection.execute(
            'UPDATE spaces SET free_dates = %s WHERE id = %s',(dates_list,id))