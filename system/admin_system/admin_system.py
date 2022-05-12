from system.system import System
from system.floors.floor import Floor 

class AdminSystem(System):
    """ Floor operations """
    def add_floor(self,name):
        self.floors.append(Floor(name))
        print("Floor added to parking lot!")

    def remove_floor(self,name):
        for i in self.floors:
            if i.name == name:
                self.floors.remove(i)
                print("Floor removed from parking lot!")
                break
    def edit_floor_name(self,name):
        for i in self.floors:
            new_floor_name = input("Enter floor name :- ")
            i.name = new_floor_name
            break

    """ Spot operations """
    def add_spot(self,floor_name,spot_name,vehicle_type):
        for i in self.floors:
            if i.name == floor_name:
                i.add_spot_to_floor(spot_name,vehicle_type)

    def edit_spot(self,floor_name,spot_name,vehicle_type):
         for i in self.floors:
            if i.name == floor_name:
                i.modify_vehicle_type(spot_name,vehicle_type)

    def remove_spot(self,floor_name,spot_name):
        for i in self.floors:
            if i.name == floor_name:
                i.remove_spot_from_floor(spot_name)

    """ Checkpoint Operations """
    def add_checkpoint_to_floor(self,floor_name,checkpoint):
        for i in self.floors:
            if i.name == floor_name:
                i.checkpoints.append(checkpoint)
                print("{} checkpoint added to floor.".format(checkpoint.name))

    def remove_checkpoint_from_floor(self,floor_name,checkpoint):
        for i in self.floors:
            check_point = [x for x in i.checkpoints if x.name == checkpoint.name]
            i.checkpoints.remove(check_point[0])
            print("{} checkpoint removed from floor.".format(checkpoint.name))
    
    def edit_checkpoint(self,floor_name,checkpoint):
        for i in self.floors:
            if i.name == floor_name:
                i.modify_checkpoint_in_floor(checkpoint)
                print("Modified checkpoint for {}".format(floor_name))
  