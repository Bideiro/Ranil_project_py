import hashlib
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator

from Database.User_Manager import UserMana
from Dialogs.DLog_Alert import DLG_Alert
from .DLog_InputAdminPass_ui import Ui_Dialog

class DLG_AdminCheckPass(QDialog, Ui_Dialog):
    
    User = UserMana()
    
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.onlyInt = QIntValidator()
        self.Input_LE.setValidator(self.onlyInt)
        self.setWindowFlags(Qt.Popup)
        
        self.ok_btn.clicked.connect(self.confirmed)
        
    def confirmed(self):
        hashedPass = hashlib.sha256(self.Input_LE.text().encode()).hexdigest() 
        if self.Input_LE.text() == '':
            Dlg = DLG_Alert(msg='Empty Passcode field!')
            Dlg.exec()
        elif  hashedPass != self.User.Pass:
            Dlg = DLG_Alert(msg='Incorrect Passcode!')
            self.done(0)
            Dlg.exec()
        else:
            self.done(1)
