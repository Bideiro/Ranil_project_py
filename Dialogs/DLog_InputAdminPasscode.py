import sys
from PyQt5.QtWidgets import QMainWindow,QDialog, QPushButton, QWidget, QMessageBox
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream
from Database.DBController import dbcont
from Dialogs.DLog_Alert import DLG_Alert
from Database.App_functions import check_user_validity
#from Screens.ForgotPass import user_input

from .DLog_InputAdminPasscode_ui import Ui_Dialog

class DLG_Change(QDialog, Ui_Dialog):
    
    def __init__(self,parent = None, userName = None):
        super().__init__(parent)
        self.user_input = userName
        self.setupUi(self)
        #self.label.setText(self.alertmsg)
        self.okBtn.clicked.connect(self.confirmed)
        self.userFinder = userName
        print(self.userFinder)
        self.db=dbcont('admin', '123456')
    def confirmed(self):
    # Validate user input
        funcmsg = check_user_validity(LevelID=1, Uname='john', pass1=self.newPcode.text(), pass2=self.verifyPcode.text(), 
                                  Fname='John', Lname='Doe', SexID=1, Phono='+639123456789', Email='john@gmail.com', 
                                  Pos=1, HDate='', BDate='', Add='')

        if funcmsg != True:
        # Show alert dialog if validation fails
            Dlg = DLG_Alert()
            Dlg.exec()
            self.done(1)
        else:
        # Validation passed, proceed to update the passcode
            uname = self.user_input 
        # Fetch old passcode from the database
            oldPcode = self.db.fetch_old_passcode_from_db(uname)  # Implement this method
            newPcode = self.newPcode.text()
            print(oldPcode)

        
        if oldPcode is None:
            QMessageBox.warning(self, "Error", "Failed to retrieve old passcode from database.")
            self.done(1)
            return
        
        newPcode = self.newPcode.text()  # Get new passcode from UI input
        
        # Update the passcode in the database
        self.db.update_user_passcode(uname, newPcode)
        
        # Optionally, show success message or perform additional actions
        QMessageBox.information(self, "Success", "Passcode updated successfully.")
        self.done(1)