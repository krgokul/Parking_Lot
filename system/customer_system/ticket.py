import datetime
class Ticket:
    count=0
    
    def __init__(self,vehicle_id=None,floor_name=None,spot_name=None,entry_name=None,entry_date=datetime.date):
        self.vehicle_id = vehicle_id
        self.floor_name = floor_name
        self.spot_name = spot_name
        self.entry_name = entry_name
        self.entry_date = entry_date
        if(self.vehicle_id != None):        
            Ticket.count +=1

    def get_vehicle_id(self):
        return self.vehicle_id
    def get_floor_name(self):
        return self.floor_name
    def get_spot_name(self):
        return self.spot_name
    def get_entry_name(self):
        return self.entry_name
    def get_entry_date(self):
        return self.entry_date

    def __str__(self):
        return "{} {} {} {} {} {}".format(self.count,self.vehicle_id,self.floor_name,self.spot_name,self.entry_name,self.entry_date)