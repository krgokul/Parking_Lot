from system.system import System
from system.floors.floor import Floor 

class AdminSystem(System):
    """
AdminSystem class : contains system operations that can be performed only by admim.

It can perform following operations such as 
1. Add new floor to parking lot.
2. Remove existing floor from parking lot.
3. Modify floor in praking lot.
4. Add new spot to floor.
5. Remove existing spot from floor.
6. Modify spot from floor.
7. Add new checkpoint to floor (Entry / Exit).
8. Remove existing checkpoint from floor (Entry / Exit).
9. Modify checkpoint from floor (Entry / Exit).

    """
    # floor operations
    def add_floor(self,name):
        super().set_floor(Floor(name))
        print("Floor added to parking lot!")

    def remove_floor(self,name):
        for floor in super().get_floors():
            if floor.get_floor_name() == name:
                super().get_floors().remove(floor)
                print("Floor removed from parking lot!")
                break
    def edit_floor_name(self,name):
        for floor in super().get_floors():
            new_floor_name = input("Enter floor name :- ")
            floor.set_floor_name(new_floor_name)
            break

    # spot operations
    def add_spot(self,floor_name,spot_name,vehicle_type):
        for floor in super().get_floors():
            if floor.get_floor_name() == floor_name:
                floor.add_spot_to_floor(spot_name,vehicle_type)

    def edit_spot(self,floor_name,spot_name,vehicle_type):
         for floor in super().get_floors():
            if floor.get_floor_name() == floor_name:
                floor.modify_vehicle_type(spot_name,vehicle_type)

    def remove_spot(self,floor_name,spot_name):
        for floor in super().get_floors():
            if floor.get_floor_name() == floor_name:
                floor.remove_spot_from_floor(spot_name)

    # checkpoint operations
    def add_checkpoint_to_floor(self,floor_name,checkpoint):
        for floor in super().get_floors():
            if floor.get_floor_name() == floor_name:
                floor.set_checkpoint(checkpoint)
                print("{} checkpoint added to floor.".format(checkpoint.get_checkpoint_name()))

    def remove_checkpoint_from_floor(self,floor_name,checkpoint_name):
        for floor in super().get_floors():
            check_point = [checkpoint for checkpoint in floor.get_checkpoints() if checkpoint.get_checkpoint_name() == checkpoint_name]
            floor.get_checkpoints().remove(check_point[0])
            print("{} checkpoint removed from floor.".format(checkpoint_name))
    
    def edit_checkpoint(self,floor_name,checkpoint):
        for floor in super().get_floors():
            if floor.get_floor_name() == floor_name:
                floor.modify_checkpoint_in_floor(checkpoint)
                print("Modified checkpoint for {}".format(floor_name))
  