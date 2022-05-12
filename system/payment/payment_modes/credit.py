from system.payment.payment import Payment

class Credit(Payment):
    """
    Credit class : is a child class of Payment class and it contains tax attribute additionally. 
    """    
    def __init__(self,price):
        super().__init__(price)
        self.tax = 10

    def get_tax(self):
        return self.tax
    
    # get total price after performing adding the taxable price to the actual price
    def get_total_price(self):
        total_amount = self.get_price() + self.get_tax()
        super().set_payment_status(True)
        return total_amount 