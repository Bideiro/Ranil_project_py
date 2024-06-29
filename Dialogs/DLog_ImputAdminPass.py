import sys
from PyQt5.QtWidgets import QMainWindow,QDialog, QPushButton, QWidget, QMessageBox


from PyQt5.QtGui import QIntValidator
from Database.App_functions import check_user_validity



from Database.DBController import dbcont
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
        
        self.ok_btn.clicked.connect(self.confirmed)
        
    def confirmed(self):
        if self.Input_LE.text() == '':
            Dlg = DLG_Alert(msg='Empty Passcode field!')
            Dlg.exec()
        elif self.Input_LE.text() != self.User.Pass:
            Dlg = DLG_Alert(msg='Incorrect Passcode!')
            self.done(0)
            Dlg.exec()
        else:
            self.done(1)
