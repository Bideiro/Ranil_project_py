

class UserMana(object):
    
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = super(UserMana, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self,'initialized'):
            self.initialized = True
        self.UID = None
        self.User = None
        self.Pass = None
        self.Level = None
        self.RUID = None
        self.WName = None
            
    def reset_UserMana(cls):
        if cls._instance:
            cls._instance.RUID = None
            cls._instance.UID = None
            cls._instance.User = None
            cls._instance.Pass = None
            cls._instance.Level = None
            cls._instance.WName = None
            cls._instance = None
        
    def set_user(self, UID, RUID, User, Pass, Level, Wname ):
        self.UID = UID
        self.User = User
        self.Pass = Pass
        self.Level = Level
        self.RUID = RUID
        self.WName = Wname
