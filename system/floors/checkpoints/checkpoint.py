
class Checkpoint:
    def __init__(self,type,name):
        self.type = type
        self.name = name
    
    def __str__(self):
        return "{} {}".format(self.name,self.type)
    
    def get_type(self):
        return self.type

    def get_checkpoint_name(self):
        return self.name
    
    def set_type(self,checkpoint_type):
        self.type = checkpoint_type
        
    def set_checkpoint_name(self,name):
        self.name = name
