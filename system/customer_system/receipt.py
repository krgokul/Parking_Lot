class Receipt:
    def __init__(self,entry_ticket=None,exit_name=None,exit_date=None,total=None,payment_status=None):
        self.entry_ticket = entry_ticket
        self.exit_name = exit_name
        self.exit_date = exit_date
        self.total = total
        if (payment_status == True):
            self.payment_status = "Paid"
        else:
            self.payment_status = "Not Paid"
    def __str__(self):
        return "{} {} {} {} {}".format(self.entry_ticket,self.exit_name,self.exit_date,self.total,self.payment_status)