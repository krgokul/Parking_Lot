import datetime

class Ticket:
    id=0
    def __init__(self,vehicle_id=None,floor_name=None,spot_name=None,entry_name=None,entry_date=datetime.date):
        self.vehicle_id = vehicle_id
        self.floor_name = floor_name
        self.spot_name = spot_name
        self.entry_name = entry_name
        self.entry_date = entry_date
        if(self.vehicle_id != None):        
            Ticket.id +=1
    def __str__(self):
        return "{} {} {} {} {} {}".format(self.id,self.vehicle_id,self.floor_name,self.spot_name,self.entry_name,self.entry_date)