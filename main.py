import datetime

class Spot:
    def __init__(self,name,vehicle_type,is_free):
        self.name = name
        self.vehicle_type = vehicle_type
        self.vehicle_id = ""
        self.is_free= is_free

    def set_filled(self):
        self.is_free = True
    
    def set_empty(self):
        self.is_free = False
    
    def __str__(self):
        return "{} {} {} {}".format(self.name,self.vehicle_id,self.vehicle_type,self.is_free)    

class Floor:
    def __init__(self,name,entry,exit):
        self.name = name
        self.entry = entry
        self.exit = exit
        self.spots = []
    
    def __str__(self):
        return "{} {} {}".format(self.name,self.entry,self.exit)
    
    def get_available_spots(self,vehicle_type):
        available_spots = [i for i in self.spots if i.vehicle_type == vehicle_type and i.is_free == False]
        return available_spots

    def add_spot_to_floor(self,spot_name,vehicle_type,is_free):
        self.spots.append(Spot(spot_name,vehicle_type,is_free))
        print ("Spot added to floor successfully!")

    def modify_vehicle_type(self,spot_name,vehicle_type):     
        for i in self.spots:
            if i.name == spot_name:
                i.vehicle_type = vehicle_type
                print("Modified vehicle type in {}!".format(spot_name))  

    def remove_spot_from_floor(self,spot_name):
        spot = [x for x in self.spots if x.name == spot_name]
        self.spots.remove(spot[0])
        print("{} remove from floor successfully.".format(spot_name))
    
    def get_entry_list(self):
        return self.entry
    
    def get_exit_list(self):
        return self.exit           

            
class System:
    floors=[]
    def __init__(self):
        pass

    def add_floor(self,name,entry,exit):
        self.floors.append(Floor(name,entry,exit))
        print("Floor added to parking lot successfully!")

    def add_spot(self,floor_name,spot_name,vehicle_type,is_free):
        for i in self.floors:
            if i.name == floor_name:
                i.add_spot_to_floor(spot_name,vehicle_type,is_free)

    def edit_spot(self,floor_name,spot_name,vehicle_type):
         for i in self.floors:
            if i.name == floor_name:
                i.modify_vehicle_type(spot_name,vehicle_type)

    def remove_spot(self,floor_name,spot_name):
        for i in self.floors:
            if i.name == floor_name:
                i.remove_spot_from_floor(spot_name)

    def add_entry_to_floor(self,floor_name):
     for i in self.floors:
        if i.name == floor_name:
            entry = input("Enter the name for entrance to floor {}\n".format(floor_name))
            i.entry.append(entry)
    
    def add_exit_to_floor(self,floor_name):
     for i in self.floors:
        if i.name == floor_name:
            exit_name = input("Enter the name for exit to floor {}\n".format(floor_name))
            i.exit.append(exit_name)

    def display_floors_and_spots(self):
        for i in self.floors:
            print(i)
            for j in i.spots:
                print(j)
            print("-----------")

    def check_availability(self,vehicle_type):
        print("-----------")
        for i in self.floors:
            print("{}".format(i.name))
            for j in i.get_available_spots(vehicle_type):
                print (j.name,j.is_free)
            print("-----------")
    
    def assign_spot_to_vehicle(self,floor_name,spot_name,vehicle_id):
        floor = [i for i in self.floors if i.name == floor_name]
        spot = [j for j in floor[0].spots if j.name == spot_name]
        spot[0].vehicle_id = vehicle_id
        spot[0].set_filled()
        
    def get_ticket(self,floor_name,spot_name,vehicle_id):
        en=""
        for i in self.floors:
           if i.name == floor_name:
                entrance =  i.get_entry_list()
                for j in range (len(entrance)):
                    print("{} - {} ".format(j,entrance[j]))
                en= entrance[int(input())]       
        self.assign_spot_to_vehicle(floor_name,spot_name,vehicle_id)
        return Ticket(vehicle_id,floor_name,spot_name,en,datetime.datetime.now())
    
    def free_spot(self,floor_name,spot_name):
        floor = [i for i in self.floors if i.name == floor_name]
        spot = [j for j in floor[0].spots if j.name == spot_name]
        spot[0].vehicle_id = ""
        spot[0].set_empty()
    
    def exit_vehicle(self,ticket):
        ex=""
        for i in self.floors:
           if i.name == ticket.floor_name:
                exit_list =  i.get_exit_list()
                for j in range (len(exit_list)):
                    print("{} - {} ".format(j,exit_list[j]))
                ex = exit_list[int(input())]
        self.free_spot(ticket.floor_name,ticket.spot_name)
        price = self.calculate_price(ticket.entry_date)
        print("0 - Cash\t1 - Credit")
        n = int(input())
        mode=""
        if (n):
            mode = "Credit"
        else:
            mode = "Cash"
        p1 = Payment(price, mode)   
        print(p1.initiate_payment())
        

    def calculate_price(self,ticket_date):
        price=0
        second = int(ticket_date.second)
        total = int(datetime.datetime.now().second) - second
        if total <= 3:
            if total >= 1:
                price =  40
            if total >= 1 and total <= 2:
                price += 30
            if total >= 2 and total <= 3:
                price += 30
        else:
            price = (total-3) * 25 + 100
        return price

class Admin:
    def __init__(self,name,system):
        self.name = name
        self.sys_obj = system

class Vehicle:
    def __init__(self,id,vehicle_type):
        self.id = id
        self.vehicle_type = vehicle_type

class Customer:
    def __init__(self,vehicle_obj,sys_obj):
        self.vehicle_obj = vehicle_obj
        self.sys_obj = sys_obj
        self.ticket = Ticket()

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

class Payment:
    def __init__(self,price,mode):
        self.price= price
        self.mode = mode
        self.payment_status= False

    def initiate_payment(self):
        self.payment_status=True
        return "Payment successfull with {}".format(self.mode)


system = System()
admin = Admin("A1",system)
v1 = Vehicle("TN60 1234","Bike")
C1 = Customer(v1,system)
admin.sys_obj.add_floor("F1",[],[])
admin.sys_obj.add_floor("F2",[],[])
admin.sys_obj.add_spot("F1","F1S1","Bike",False)
admin.sys_obj.add_spot("F1","F1S2","Bike",False)
admin.sys_obj.add_entry_to_floor("F1")
admin.sys_obj.add_exit_to_floor("F1")
C1.ticket = C1.sys_obj.get_ticket("F1","F1S1",C1.vehicle_obj.id)
C1.sys_obj.display_floors_and_spots()
C1.sys_obj.exit_vehicle(C1.ticket)