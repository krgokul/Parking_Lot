from system.payment.payment import Payment

class Cash(Payment):

    """
    Cash class : is a child class of Payment class and it contains deduction attribute additionally. 
    """ 
    def __init__(self,price):
        super().__init__(price)
        self.deduction = 10

    def get_deduction(self):
        return self.deduction

    # get total pric after performing reducing the deduction price to actual price
    def get_total_price(self):
        total_amount = self.get_price() + self.get_deduction()
        super().set_payment_status(True)
        return total_amount 