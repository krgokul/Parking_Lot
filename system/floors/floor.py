from system.floors.spots.spot import Spot

class Floor:
    def __init__(self,name):
        self.name = name
        self.checkpoints =[]
        self.spots = []
    
    def get_floor_name(self):
        return self.name
        
    def __str__(self):
        return "{} {}".format(self.name,self.checkpoints)
    
    def get_available_spots(self,vehicle_type):
        available_spots = [i for i in self.spots if i.vehicle_type == vehicle_type and i.is_occupied == False]
        return available_spots

    def add_spot_to_floor(self,spot_name,vehicle_type):
        self.spots.append(Spot(spot_name,vehicle_type))
        print ("Spot added to floor!")

    def modify_vehicle_type(self,spot_name,vehicle_type):     
        for i in self.spots:
            if i.name == spot_name:
                old_type = i.vehicle_type
                i.vehicle_type = vehicle_type
                print("Modified vehicle type from {} to {} for {}!".format(old_type,vehicle_type,spot_name))  

    def remove_spot_from_floor(self,spot_name):
        spot = [x for x in self.spots if x.name == spot_name]
        self.spots.remove(spot[0])
        print("{} spot removed from floor.".format(spot_name))
    
    def modify_checkpoint_in_floor(self,checkpoint):
        for i in self.checkpoints:
          if i.name == checkpoint.name:
            change_type = input("Enter type :-")
            change_checkpoint_name =  input("Enter name :-")
            i.name = change_checkpoint_name
            i.type = change_type

    def get_entry_list(self):
        entry = []
        for i in self.checkpoints:
            if i.type == "entrance":
                entry.append(i.get_checkpoint_name())
        return entry
    
    def get_exit_list(self):
        exit = []
        for i in self.checkpoints:
            if i.type == "exit":
                exit.append(i.get_checkpoint_name())
        return exit        
     