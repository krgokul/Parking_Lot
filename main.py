""" Admin functionalities """
from system.admin_system.admin_system import AdminSystem
from system.customer_system.customer_system import CustomerSystem
from system.system import System
from actors.actor import Admin,Customer,Vehicle

from system.floors.floor import Floor 
from system.floors.spots.spot import Spot
from system.floors.checkpoints.checkpoint import Checkpoint

from system.payment.payment_modes.credit import Credit
from system.payment.payment_modes.cash import Cash

system = System()
admin_system = AdminSystem()
admin = Admin("A1")

admin_system.add_floor("F1")
admin_system.add_spot("F1","F1S1","Car")
# admin.sys_obj.remove_spot("F1","F1S1")

admin_system.add_spot("F1","F1S2","Car")
admin_system.add_spot("F1","F1S3","Bike")
admin_system.add_spot("F1","F1S4","Bike")
# admin_system.edit_spot("F1","F1S1","Bike")

ch1 = Checkpoint("entrance","F1EN1")
ch2 = Checkpoint("exit","F1EX1")
ch3 = Checkpoint("entrance","F1EN2")

admin_system.add_checkpoint_to_floor("F1",ch1)
admin_system.add_checkpoint_to_floor("F1",ch2)
admin_system.add_checkpoint_to_floor("F1",ch3)
system.display_entrance("F1")
system.display_exit("F1")

# admin.sys_obj.edit_checkpoint("F1",ch2)
# admin.sys_obj.remove_checkpoint_from_floor("F1",ch1)
admin_system.display_availability("Bike")
# admin_system.display_floors_and_spots()

""" Customer functionalities """
# customer_system = CustomerSystem()
# v1 = Vehicle("TN60 1234","Bike")
# c1 = Customer(v1)

# customer_system.display_availability("Car")
# en = customer_system.choose_entrance("F1")
# c1.set_ticket(customer_system.get_ticket("F1","F1S2",en,c1.get_vehicle_id()))
# # print(C1.ticket)
# ex = customer_system.choose_exit("F1")
# c1.set_receipt(customer_system.exit_vehicle(c1.get_ticket(),ex,"Credit"))
# print(c1.get_receipt())
