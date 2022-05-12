class Receipt:
    """
    Recepit class holds ticekt object, exit_name,exit_date,total
    """
    def __init__(self,entry_ticket=None,exit_name=None,exit_date=None,total_amt=None,payment_status=None):
        self.entry_ticket = entry_ticket
        self.exit_name = exit_name
        self.exit_date = exit_date
        self.total_amt = total_amt
        if payment_status:
            self.payment_status = "Paid"
        else:
            self.payment_status = "Not Paid"
    def __str__(self):
        return "{} {} {} {} {}".format(self.entry_ticket,self.exit_name,self.exit_date,self.total_amt,self.payment_status)