from system.payment.payment import Payment

class Cash(Payment):
    def __init__(self,price):
        super().__init__(price)
        self.deduction = 10
   
    def get_deduction(self):
        return self.deduction

    def initiate_payment(self):
        total_amount = self.get_price() + self.get_deduction()
        self.set_payment_status(True)
        return (total_amount,self.get_payment_status())