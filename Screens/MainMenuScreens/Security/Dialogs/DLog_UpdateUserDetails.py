
from PyQt5.QtWidgets import QDialog, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from matplotlib.testing import set_font_settings_for_testing
from PyQt5.QtGui import QIntValidator

from .DLog_UpdateUserDetails_ui import Ui_Dialog
from Dialogs.DLog_Alert import DLG_Alert
from Database.DBController import dbcont
from Database.App_functions import check_user_validity

class DLG_Edit_User(QDialog, Ui_Dialog):
    
    disable_btnsgl = QtCore.pyqtSignal()
    update_btnsgl = QtCore.pyqtSignal()
    db = dbcont()
    
    def __init__(self, Ulist = None,parent = None):
        super().__init__(parent)
        
        self.currlist = Ulist
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.onlyInt = QIntValidator()
        self.Pass_LE.setValidator(self.onlyInt)
        self.CPass_LE.setValidator(self.onlyInt)
        self.Phono_LE.setValidator(self.onlyInt)
        
        self.back_btn.clicked.connect(lambda: self.done(0))
        self.update_btn.clicked.connect(self.init_update_user)
        self.Pass_btn.clicked.connect(self.show_passcode)
        self.CPass_btn.clicked.connect(self.show_passcode)
        self.Disable_btn.clicked.connect(self.set_disabled)
        
        self.Sex_CB.addItems(self.db.get_sex(all= True))
        self.ULevel_CB.addItems(self.db.get_levels(all= True))
        self.FName_LE.setText(self.currlist[5])
        self.LName_LE.setText(self.currlist[6])
        self.UName_LE.setText(self.currlist[3])
        self.ULevel_CB.setCurrentIndex(int(self.currlist[1]))
        self.Email_LE.setText(self.currlist[9])
        self.BDate_DE.setDate(self.currlist[12])
        self.Sex_CB.setCurrentIndex(int(self.currlist[7]))
        self.Phono_LE.setText('+' + self.currlist[8])
        self.Pos_LE.setText(self.currlist[10])
        self.DHired_DE.setDate(self.currlist[11])
        self.Address_LE.setText(self.currlist[13])
        
        self.switch_inputs(active=self.db.access_status_user(RUID=self.currlist[2]))
        self.show_passcode()
        
    def set_disabled(self):
        active = self.db.access_status_user(RUID=self.currlist[2])
        if active == 1:
            self.db.access_status_user(RUID= self.currlist[2], status= 0)
        else:
            self.db.access_status_user(RUID= self.currlist[2], status= 1)
        curr = self.db.access_status_user(RUID=self.currlist[2])
        self.switch_inputs(curr)
        
    def switch_inputs(self, active):
        if active == 1:
            self.Disable_btn.setText('Disable')
            self.FName_LE.setEnabled(True)
            self.LName_LE.setEnabled(True)
            self.UName_LE.setEnabled(True)
            self.Email_LE.setEnabled(True)
            self.ULevel_CB.setEnabled(True)
            self.BDate_DE.setEnabled(True)
            self.Sex_CB.setEnabled(True)
            self.Pos_LE.setEnabled(True)
            self.Phono_LE.setEnabled(True)
            self.DHired_DE.setEnabled(True)
            self.Pass_LE.setEnabled(True)
            self.CPass_LE.setEnabled(True)
            self.Address_LE.setEnabled(True)
            
            self.Pass_btn.setEnabled(True)
            self.CPass_btn.setEnabled(True)
        else:
            self.Disable_btn.setText('Enable')
            self.FName_LE.setEnabled(False)
            self.LName_LE.setEnabled(False)
            self.UName_LE.setEnabled(False)
            self.Email_LE.setEnabled(False)
            self.ULevel_CB.setEnabled(False)
            self.BDate_DE.setEnabled(False)
            self.Sex_CB.setEnabled(False)
            self.Pos_LE.setEnabled(False)
            self.Phono_LE.setEnabled(False)
            self.DHired_DE.setEnabled(False)
            self.Pass_LE.setEnabled(False)
            self.CPass_LE.setEnabled(False)
            self.Address_LE.setEnabled(False)
            
            self.Pass_btn.setEnabled(False)
            self.CPass_btn.setEnabled(False)
        
        
    def show_passcode(self):
        
        if self.Pass_btn.isChecked():
            self.Pass_LE.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.Pass_LE.setEchoMode(QLineEdit.EchoMode.Password)
            
        if self.CPass_btn.isChecked():
            self.CPass_LE.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.CPass_LE.setEchoMode(QLineEdit.EchoMode.Password)
        
    def init_update_user(self):
        if len(self.Pass_LE.text()) <= 6:
            funcmsg = check_user_validity(nochangepw= True,
                            Fname= self.FName_LE.text(), Lname= self.LName_LE.text(),
                            Uname= self.UName_LE.text(), Email= self.Email_LE.text(),
                            LevelID= self.ULevel_CB.currentIndex(), Bdate= self.BDate_DE.date().toPyDate(),
                            SexID= self.Sex_CB.currentIndex(), Pos= self.Pos_LE.text(),
                            Phono= self.Phono_LE.text(), Hdate= self.DHired_DE.date().toPyDate(), 
                            Add= self.Address_LE.text(),
                            )
        else:
            funcmsg = check_user_validity(
                                Fname= self.FName_LE.text(), Lname= self.LName_LE.text(),
                                Uname= self.UName_LE.text(), Email= self.Email_LE.text(),
                                LevelID= self.ULevel_CB.currentIndex(), Bdate= self.BDate_DE.date().toPyDate(),
                                SexID= self.Sex_CB.currentIndex(), Pos= self.Pos_LE.text(),
                                Phono= self.Phono_LE.text(), Hdate= self.DHired_DE.date().toPyDate(), 
                                Add= self.Address_LE.text(), pass1= self.Pass_LE.text(),
                                pass2= self.CPass_LE.text()
                                )
        if funcmsg != True:
            Dlg = DLG_Alert(msg= funcmsg)
            Dlg.exec()
        else:
            self.confirmed_update()
    
    def confirmed_update(self):
        Dlg =  DLG_Alert()
        Dlg.exec()
        self.done(1)