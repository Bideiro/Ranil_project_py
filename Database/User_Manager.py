

class UserMana(object):
    
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = super(UserMana, cls).__new__(cls,*args,**kwargs)
        return cls._instance
    
    def __init__(self,UserId, User, Pass ,Utype):
        if not hasattr(self,'initialized'):
            self.UserId = UserId
            self.User = User
            self.Pass = Pass
            self.UType = Utype
            
            
    def reset_UserMana(self):
        _instance = None
