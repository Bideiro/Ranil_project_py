
from PyQt5.QtWidgets import QMainWindow,QDialog, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream
from PyQt5 import QtWidgets, QtGui, QtCore

from .Dlog_editprod_ui import Ui_Dialog
from Dialogs.DLog_Alert import DLG_Alert
from Database.App_functions import check_user_validity
from Database.DBController import dbcont

class DLG_Edit_User(QDialog, Ui_Dialog):
    
    update_btnsgl = QtCore.pyqtSignal()
    
    def __init__(self, Ulist = None,parent = None):
        super().__init__(parent)
        
        self.currlist = Ulist
        self.setupUi(self)
        self.db = dbcont('admin',132456)
        
        self.back_btn.clicked.connect(lambda: self.done(0))
        self.update_btn.clicked.connect(self.init_update_user)
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.Unit_CB.addItems(self.db.get_id_value(unit=True))
        self.ULevel_CB.addItems(self.db.get_id_value(level= True))
        
    def init_update_user(self):
        funcmsg = check_user_validity(LevelID= self.ULevel_CB.currentIndex(), Uname= self.UName_LE.text(),
                            pass1= '1234560',pass2 = '123456', 
                            Fname= self.FName_LE.text(), Lname= self.LName_LE.text(),
                            SexID= self.Sex_CB.currentIndex(), Phono= self.Phono_LE.text(),
                            Email= self.Email_LE.text(), Pos= self.Pos_LE.text())
        if funcmsg != True:
            Dlg = DLG_Alert(msg= funcmsg)
            Dlg.exec()
        else:
            self.confirmed_update()
    
    def confirmed_update(self):
        Dlg =  DLG_Alert()
        Dlg.exec()
        self.done(1)