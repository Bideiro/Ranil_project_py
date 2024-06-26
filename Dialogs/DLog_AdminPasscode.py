import sys
from PyQt5.QtWidgets import QMainWindow,QDialog, QPushButton, QWidget, QMessageBox
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QIntValidator
from Database.DBController import dbcont
from Dialogs.DLog_Alert import DLG_Alert
from Database.App_functions import check_user_validity

from .DLog_AdminPasscode_ui import Ui_Dialog

class DLG_AdminPass(QDialog, Ui_Dialog):
    
    def __init__(self,parent = None, RUID = None, User = None, Email = None, confirmation =None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.RUID = RUID
        self.User = User
        self.Email = Email
        self.Confirm = confirmation
        self.db=dbcont('admin', '123456')
        
        
        self.Confirm_btn.clicked.connect(self.confirmed)
        self.onlyInt = QIntValidator()
        self.PCode_LE.setValidator(self.onlyInt)
        self.VPCode_LE.setValidator(self.onlyInt)
        
    def confirmed(self):
        if self.Confirm:
            pass
        
        else:
            if self.PCode_LE.text() == '' or self.VPCode_LE.text() == '':
                Dlg = DLG_Alert(msg='Empty Passcode field!')
                Dlg.exec()
            elif self.PCode_LE.text() != self.PCode_LE.text():
                Dlg = DLG_Alert(msg='Passcodes dont match!')
                Dlg.exec()
            else:
                self.done(1)
        #     oldPcode = self.db.fetch_old_passcode_from_db(self.User)
        #     newPcode = self.newPcode.text()
        
        # if oldPcode is None:
        #     QMessageBox.warning(self, "Error", "Failed to retrieve old passcode from database.")
        #     self.done(1)
        #     return
        
        # newPcode = self.newPcode.text()  # Get new passcode from UI input
        
        # # Update the passcode in the database
        # self.db.update_user_passcode(uname, newPcode)
        
        # # Optionally, show success message or perform additional actions
        # QMessageBox.information(self, "Success", "Passcode updated successfully.")
        # self.done(1)