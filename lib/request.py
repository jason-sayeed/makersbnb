class Request:

    def __init__(self, id, spaceid, date, guestid, hostid, approved):
        self.id = id
        self.spaceid = spaceid
        self.date = date
        self.guestid = guestid
        self.hostid = hostid
        self.approved = approved

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Request({self.id}, {self.spaceid}, {self.date}, {self.guestid}, {self.hostid}, {self.approved})"