class System:
    floors=[]
    def display_floors_and_spots(self):
        for i in self.floors:
            print("--------------")
            print("Floor name:-",i.get_floor_name())
            print("Entrance:-")
            for en in i.get_entry_list():
                print(en)
            print("\nExit:-")
            for ex in i.get_exit_list():
                print(ex)
            print("\nSpots:-")
            for sp in i.spots:
                print(sp)
            print("--------------")

    def display_availability(self,vehicle_type):
        print("-----------")
        for i in self.floors:
            print("{}".format(i.get_floor_name()))
            spot_list = i.get_available_spots(vehicle_type)
            if(len(spot_list) == 0):
                print("{} parking is full".format(vehicle_type))
            for j in spot_list:
                print (j.get_spot_name())
            print("-----------")
    
    def display_entrance(self,floor_name):
        for i in self.floors:
           if i.get_floor_name() == floor_name:
                entrance =  i.get_entry_list()
                for j in entrance:
                    print(j)
    
    def display_exit(self,floor_name):
        for i in self.floors:
           if i.get_floor_name() == floor_name:
                exit =  i.get_exit_list()
                for j in exit:
                    print(j)

