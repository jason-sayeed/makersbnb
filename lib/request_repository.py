from lib.request import Request
from datetime import date

class RequestRepository:
    def __init__(self, connection):
        self._connection = connection

    def add(self, request):
        rows = self._connection.execute(
            'INSERT into requests(spaceid, date, guestid, hostid, approved) VALUES (%s, %s, %s, %s, %s) RETURNING id', [
                request.spaceid, request.date, request.guestid, request.hostid, request.approved
                ]
        )
        request.id = rows[0]['id']
        return None

    def all(self):
        rows = self._connection.execute(
            'SELECT * FROM requests'
        )
        request = []
        for row in rows:
            item = Request(row['id'], row['spaceid'], row['date'], row['guestid'], row['hostid'], row['approved'])
            request.append(item)
        return request
    
    def get_request_by_id(self, id):
        query = 'SELECT * FROM requests WHERE id = %s'
        result = self._connection.execute(query, (id, ))
        if result:
            row = result[0]
            request = Request(row['id'], row['spaceid'], row['date'], row['guestid'], row['hostid'], row['approved'])
            return request
        else:
            return None

    def get_request_by_spaceid(self, spaceid):
        query = 'SELECT * FROM requests WHERE spaceid = %s'
        result = self._connection.execute(query, (spaceid, ))
        if result:
            row = result[0]
            request = Request(row['id'], row['spaceid'], row['date'], row['guestid'], row['hostid'], row['approved'])
            return request
        else:
            return None


    def get_request_by_guestid(self, guestid):
        query = 'SELECT * FROM requests WHERE guestid = %s'
        result = self._connection.execute(query, (guestid, ))
        if result:
            row = result[0]
            request = Request(row['id'], row['spaceid'], row['date'], row['guestid'], row['hostid'], row['approved'])
            return request
        else:
            return None

    def get_request_by_hostid(self, hostid):
        query = 'SELECT * FROM requests WHERE hostid = %s'
        result = self._connection.execute(query, (hostid, ))
        if result:
            row = result[0]
            request = Request(row['id'], row['spaceid'], row['date'], row['guestid'], row['hostid'], row['approved'])
            return request
        else:
            return None

    def approve_request(self, request_id):
        query = 'UPDATE requests SET approved = true WHERE id = %s'
        self._connection.execute(query, (request_id,))

