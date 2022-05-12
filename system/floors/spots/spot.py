class Spot:
    def __init__(self,name,vehicle_type):
        self.name = name
        self.vehicle_type = vehicle_type
        self.vehicle_id = ""
        self.is_occupied = False

    def set_spot_status(self,spot_status):
        self.is_occupied = spot_status

    def get_spot_name(self):
        return self.name
    def get_spot_status(self):
        return self.is_occupied
    def get_spot_type(self):
        return self.vehicle_type
    
    def __str__(self):
        return "{} {} {} {}".format(self.name,self.vehicle_id,self.vehicle_type,self.is_occupied)    