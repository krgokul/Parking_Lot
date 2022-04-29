import datetime

class Spot:
    def __init__(self,name,vehicle_type,is_occupied):
        self.name = name
        self.vehicle_type = vehicle_type
        self.vehicle_id = ""
        self.is_occupied = is_occupied

    def set_spot_status(self,spot_status):
        self.is_occupied = spot_status
    
    
    def __str__(self):
        return "{} {} {} {}".format(self.name,self.vehicle_id,self.vehicle_type,self.is_occupied)    

class Floor:
    def __init__(self,name):
        self.name = name
        self.checkpoints =[]
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
        entry = []
        for i in self.checkpoints:
            if i.type == "entrance":
                entry.append(i.name)
        return entry
    
    def get_exit_list(self):
        entry = []
        for i in self.checkpoints:
            if i.type == "exit":
                entry.append(i.name)
        return entry         

            
class System:
    floors=[]

    def add_floor(self,name):
        self.floors.append(Floor(name))
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

    def add_checkpoint_to_floor(self,floor_name,checkpoint):
        for i in self.floors:
            if i.name == floor_name:
                i.checkpoints.append(checkpoint)
                print("{} added successfully".format(checkpoint.name))

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
    
    def choose_entrance(self,floor_name):
        en=""
        for i in self.floors:
           if i.name == floor_name:
                entrance =  i.get_entry_list()
                for j in range (len(entrance)):
                    print("{} - {} ".format(j,entrance[j]))
                en= entrance[int(input())]   
        return en
    
    def choose_exit(self,floor_name):
        ex=""
        for i in self.floors:
           if i.name == floor_name:
                exit_list =  i.get_exit_list()
                for j in range (len(exit_list)):
                    print("{} - {} ".format(j,exit_list[j]))
                ex = exit_list[int(input())]
        return ex
    
    def assign_spot_to_vehicle(self,floor_name,spot_name,vehicle_id):
        floor = [i for i in self.floors if i.name == floor_name]
        spot = [j for j in floor[0].spots if j.name == spot_name]
        spot[0].vehicle_id = vehicle_id
        spot[0].set_spot_status(True)
        
    def get_ticket(self,floor_name,spot_name,entrance_name,vehicle_id):
        self.assign_spot_to_vehicle(floor_name,spot_name,vehicle_id)
        return Ticket(vehicle_id,floor_name,spot_name,entrance_name,datetime.datetime.now())
    
    def free_spot(self,floor_name,spot_name):
        floor = [i for i in self.floors if i.name == floor_name]
        spot = [j for j in floor[0].spots if j.name == spot_name]
        spot[0].vehicle_id = ""
        spot[0].set_spot_status(False)
    
    def payment_mode(self):
        payment_mode=["Credit","Cash"]
        print("0 - Cash\t1 - Credit")
        n = int(input())
        return payment_mode[n]
        
    def exit_vehicle(self,ticket,exit_name,payment_type):
        self.free_spot(ticket.floor_name,ticket.spot_name)
        price = self.calculate_price(ticket.entry_date)
        if payment_type == "Credit":
            pay = Credit(price)
        else:
            pay = Cash(price)
        result = pay.initiate_payment()
        return Receipt(ticket,exit_name,datetime.datetime.now(),result[0],result[1])
    
    def calculate_price(self,entry_time):
        price=0
        second = int(entry_time.second)
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

class Payment:
    def __init__(self,price):
        self.price= price
        self.payment_status = False

class Credit(Payment):
    def __init__(self,price):
        super().__init__(price)
        self.tax = 10

    def initiate_payment(self):
        total_amount = self.price + self.tax
        self.payment_status = True
        return (total_amount,self.payment_status)
        
class Cash(Payment):
    def __init__(self,price):
        super().__init__(price)
        self.deduction = 10

    def initiate_payment(self):
        total_amount = self.price + self.deduction
        self.payment_status = True
        return (total_amount,self.payment_status)

class Receipt:
    def __init__(self,entry_ticket,exit_name,exit_date,total,payment_status):
        self.entry_ticket = entry_ticket
        self.exit_name = exit_name
        self.exit_date = exit_date
        self.total = total
        if (payment_status == True):
            self.payment_status = "Paid"
        else:
            self.payment_status = "Not Paid"
    def __str__(self):
        return "{} {} {} {} {}".format(self.entry_ticket,self.exit_name,self.exit_date,self.total,self.payment_status)

    
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

class Checkpoint:
    def __init__(self,type,name):
        self.type = type
        self.name = name
    def __str__(self):
        return "{} {}".format(self.name,self.type)

system = System()
admin = Admin("A1",system)
v1 = Vehicle("TN60 1234","Bike")
C1 = Customer(v1,system)

admin.sys_obj.add_floor("F1")

ch1 = Checkpoint("entrance","F1EN1")
ch2 = Checkpoint("entrance","F1EN2")
ch3 = Checkpoint("entrance","F1EN3")

admin.sys_obj.add_checkpoint_to_floor("F1",ch1)
admin.sys_obj.add_checkpoint_to_floor("F1",ch2)
admin.sys_obj.add_checkpoint_to_floor("F1",ch3)
entr = admin.sys_obj.choose_entrance("F1")

s1 =  System()