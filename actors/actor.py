from system.customer_system.customer_system import Ticket
from system.customer_system.customer_system import Receipt 

class Admin:
    def __init__(self,name):
        self.name = name
    def get_name(self):
        return self.name

class Vehicle:
    def __init__(self,id,vehicle_type):
        self.id = id
        self.vehicle_type = vehicle_type

class Customer:
    def __init__(self,vehicle_obj):
        self.vehicle_obj = vehicle_obj
        self.ticket = Ticket()
        self.receipt = Receipt()
    def get_ticket(self):
        return self.ticket
    def get_receipt(self):
        return self.receipt
    def set_ticket(self,ticket):
        self.ticket=ticket
    def set_receipt(self,receipt):
        self.receipt = receipt
    def get_vehicle_id(self):
        return self.vehicle_obj.id