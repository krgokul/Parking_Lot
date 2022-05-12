from system.payment.payment import Payment

class Credit(Payment):
    
    def __init__(self,price):
        super().__init__(price)
        self.tax = 10

    def get_tax(self):
        return self.tax

    def initiate_payment(self):
        total_amount = self.price + self.tax
        self.set_payment_status(True)
        return (total_amount,self.get_payment_status())