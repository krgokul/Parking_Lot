from system.system import System
from system.floors.floor import Floor 
from system.customer_system.ticket import Ticket
from system.customer_system.receipt import Receipt
from system.payment.payment_modes.credit import Credit
from system.payment.payment_modes.cash import Cash
import datetime

class CustomerSystem(System):
    """
CustomerSystem class : contains system operations that can be performed only by customer.
It contains following operations such as
1. Get ticket for vehicle parking.
2. Display payment mode.
3. Exit vehicle and get receipt from parking lot .

    """
    # Assign vehicle to spot in a floor
    def assign_spot_to_vehicle(self,floor_name,spot_name,vehicle_id):
        floor = [floor for floor in self.get_floors() if floor.get_floor_name()  == floor_name]
        spot = [spot for spot in floor[0].get_spots() if spot.get_spot_name()  == spot_name]
        spot[0].set_vehicle_id(vehicle_id)
        spot[0].set_spot_status(True)

    # Get ticket for parking vehicle
    def get_ticket(self,floor_name,spot_name,entrance_name,vehicle_id):
        self.assign_spot_to_vehicle(floor_name,spot_name,vehicle_id)
        return Ticket(vehicle_id,floor_name,spot_name,entrance_name,datetime.datetime.now())
    
    #  free vehilce spot from floor
    def free_spot(self,floor_name,spot_name):
        floor = [floor for floor in self.get_floors() if floor.get_floor_name()  == floor_name]
        spot = [spot for spot in floor[0].get_spots() if spot.get_spot_name()  == spot_name]
        spot[0].set_vehicle_id("")
        spot[0].set_spot_status(False)
    
    # Display payment options
    def display_payment_mode(self):
        print("Credit or Cash")

    # Exit vehicle from parking lot  
    def exit_vehicle(self,ticket,exit_name,payment_type):
        self.free_spot(ticket.get_floor_name(),ticket.get_spot_name())
        price = self.calculate_price(ticket.get_entry_date())
        if payment_type == "Credit":
            pay = Credit(price)
        else:
            pay = Cash(price)

        return Receipt(ticket,exit_name,datetime.datetime.now(),pay.get_total_price(),pay.get_payment_status())
    
    # Calculate price for parking duration of the vehicle 
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
