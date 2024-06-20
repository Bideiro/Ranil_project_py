
from PyQt5.QtWidgets import QMainWindow,QDialog, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream
from PyQt5 import QtWidgets, QtGui, QtCore

from .DLog_UpdateUserDetails_ui import Ui_Dialog
from Dialogs.DLog_Alert import DLG_Alert
from Database.DBController import dbcont
from Database.App_functions import check_user_validity

class DLG_Edit_User(QDialog, Ui_Dialog):
    
    update_btnsgl = QtCore.pyqtSignal()
    
    def __init__(self, Ulist = None,parent = None):
        super().__init__(parent)
        
        self.currlist = Ulist
        self.setupUi(self)
        self.db = dbcont('admin', 123456)
        
        self.back_btn.clicked.connect(lambda: self.done(0))
        self.update_btn.clicked.connect(self.init_update_user)
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.Sex_CB.addItems(self.db.get_id_value(sex= True))
        self.ULevel_CB.addItems(self.db.get_id_value(level= True))
        self.FName_LE.setText(self.currlist[4])
        self.LName_LE.setText(self.currlist[5])
        self.UName_LE.setText(self.currlist[2])
        self.ULevel_CB.setCurrentIndex(int(self.currlist[1]))
        self.Email_LE.setText(self.currlist[8])
        self.BDate_DE.setDate(self.currlist[11])
        self.Sex_CB.setCurrentIndex(int(self.currlist[6]))
        self.Phono_LE.setText('+' + self.currlist[7])
        self.Pos_LE.setText(self.currlist[9])
        self.DHired_DE.setDate(self.currlist[10])
        self.Address_LE.setText(self.currlist[12])
        print(int(self.currlist[6]))
        print(self.currlist[6])
        
    def init_update_user(self):
        funcmsg = check_user_validity(LevelID= self.ULevel_CB.currentIndex(), Uname= self.UName_LE.text(),
                            pass1= '123456',pass2 = '123456', 
                            Fname= self.FName_LE.text(), Lname= self.LName_LE.text(),
                            SexID= self.Sex_CB.currentIndex(), Phono= self.Phono_LE.text(),
                            Email= self.Email_LE.text(), Pos= self.Pos_LE.text(),
                            HDate= self.DHired_DE.date().toPyDate(), BDate= self.BDate_DE.date().toPyDate(),
                            Add= self.Address_LE.text())
        if funcmsg != True:
            Dlg = DLG_Alert(msg= funcmsg)
            Dlg.exec()
        else:
            self.confirmed_update()
    
    def confirmed_update(self):
        Dlg =  DLG_Alert()
        Dlg.exec()
        self.done(1)