from system.system import System
from system.floors.floor import Floor 
from system.customer_system.ticket import Ticket
from system.customer_system.receipt import Receipt
from system.payment.payment_modes.credit import Credit
from system.payment.payment_modes.cash import Cash

import datetime

class CustomerSystem(System):
    def choose_entrance(self,floor_name):
        en=""
        for i in self.floors:
           if i.name == floor_name:
                entrance =  i.get_entry_list()
                for j in range (len(entrance)):
                    print("{} - {} ".format(j,entrance[j]))
                en = entrance[int(input())]   
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
