from system.customer_system.ticket import Ticket
from system.customer_system.receipt import Receipt 

"""
Actor class :- represents actors or participants who can access the parking lot.
"""
class Admin:
    def __init__(self,name):
        self.name = name
    def get_name(self):
        return self.name

class Vehicle:
    def __init__(self,id,vehicle_type):
        self.id = id
        self.vehicle_type = vehicle_type
    
    def get_vehicle_id(self):
        return self.id

class Customer:
    def __init__(self,vehicle_obj):
        self.vehicle_obj = vehicle_obj
        self.ticket = Ticket()
        self.receipt = Receipt()

    # get vehicle id from Customer class
    def get_vehicle_id(self):
        return self.vehicle_obj.get_vehicle_id()

    # get ticket object from Customer class
    def get_ticket(self):
        return self.ticket

    # set ticket object to Customer class
    def set_ticket(self,ticket):
        self.ticket=ticket

    # get receipt object from Customer class
    def get_receipt(self):
        return self.receipt

    # set receipt object to Customer class
    def set_receipt(self,receipt):
        self.receipt = receipt
    
    