class System:
    """
    System class :- contains common operation that are performed by both admin and customer.
    
    It contains following operations such as
1. Display floors and spots in parking lot.
2. Display available spots for parking vehicle.
3. Display entrances in floor.
4. Display exits in floor.

    """
    floors=[]

    def get_floors(self):
        return System.floors

    def set_floor(self,floor):
        System.floors.append(floor)
    
    def display_floors_and_spots(self):
        for floor in self.get_floors():
            print("--------------")
            print("Floor name:-",floor.get_floor_name())
            print("Entrance:-")
            for entrance in floor.get_entry_list():
                print(entrance)
            print("\nExit:-")
            for exit in floor.get_exit_list():
                print(exit)
            print("\nSpots:-")
            for spot in floor.get_spots():
                print(spot)
            print("--------------")

    def display_availability(self,vehicle_type):
        print("-----------")
        for floor in self.get_floors():
            print("{}".format(floor.get_floor_name()))
            spot_list = floor.get_available_spots(vehicle_type)
            if(len(spot_list) == 0):
                print("{} parking is full".format(vehicle_type))
            for spot in spot_list:
                print (spot.get_spot_name())
            print("-----------")
    
    def display_entrances(self,floor_name):
        for floor in self.get_floors():
           if floor.get_floor_name() == floor_name:
                entrance_list =  floor.get_entry_list()
                for entrance in entrance_list:
                    print(entrance)

    def display_exits(self,floor_name):
        for floor in self.get_floors():
           if floor.get_floor_name() == floor_name:
                exit_list =  floor.get_exit_list()
                for exit in exit_list:
                    print(exit)

