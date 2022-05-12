from system.floors.spots.spot import Spot

class Floor:
    """
    Floor class : contains names,list of spot object and checkpoint object
    """
    def __init__(self,name):
        self.name = name
        self.checkpoints =[]
        self.spots = []
    
    def get_checkpoints(self):
        return self.checkpoints
    
    def set_checkpoint(self,checkpoint):
        self.checkpoints.append(checkpoint)

    def get_spots(self):
        return self.spots

    def set_spot(self,spot):
        self.spots.append(spot)

    def get_floor_name(self):
        return self.name
    
    def set_floor_name(self,name):
        self.name = name
        
    def __str__(self):
        return "{} {}".format(self.name,self.checkpoints)
    
    def get_available_spots(self,vehicle_type):
        available_spots = [spot for spot in self.get_spots() if spot.get_spot_type() == vehicle_type and spot.get_spot_status() == False]
        return available_spots

    def add_spot_to_floor(self,spot_name,vehicle_type):
        self.set_spot(Spot(spot_name,vehicle_type))
        print ("Spot added to floor!")

    def modify_vehicle_type(self,spot_name,vehicle_type):     
        for spot in self.get_spots():
            if spot.get_spot_name() == spot_name:
                old_type = spot.get_spot_type()
                spot.set_spot_type(vehicle_type)
                print("Modified vehicle type from {} to {} for {}!".format(old_type,vehicle_type,spot_name))  

    def remove_spot_from_floor(self,spot_name):
        spot = [spot for spot in self.spots if spot.get_spot_name() == spot_name]
        self.get_spots().remove(spot[0])
        print("{} spot removed from floor.".format(spot_name))
    
    def modify_checkpoint_in_floor(self,prior_checkpoint):
        for checkpoint in self.get_checkpoints():
          if checkpoint.get_checkpoint_name() == prior_checkpoint.get_checkpoint_name():
            modified_checkpoint_type = input("Enter type :-")
            modified_checkpoint_name =  input("Enter name :-")
            checkpoint.set_checkpoint_name(modified_checkpoint_name)
            checkpoint.set_type(modified_checkpoint_type)

    def get_entry_list(self):
        entry = []
        for checkpoint in self.get_checkpoints():
            if checkpoint.get_type() == "entrance":
                entry.append(checkpoint.get_checkpoint_name())
        return entry
    
    def get_exit_list(self):
        exit = []
        for checkpoint in self.get_checkpoints():
            if checkpoint.get_type() == "exit":
                exit.append(checkpoint.get_checkpoint_name())
        return exit        
     