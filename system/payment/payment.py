class Payment:
    
    def __init__(self,price):
        self.price= price
        self.payment_status = False
    
    def get_price(self):
        return self.price

    def set_price(self,price):
        self.price=price
    
    def set_payment_status(self,status):
        self.payment_status = status
    
    def get_payment_status(self):
        return self.payment_status