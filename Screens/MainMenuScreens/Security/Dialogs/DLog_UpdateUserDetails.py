
from PyQt5.QtWidgets import QMainWindow,QDialog, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .DLog_UpdateUserDetails_ui import Ui_Dialog
from Dialogs.DLog_Alert import DLG_Alert
from Database.DBController import dbcont

class DLG_Edit_User(QDialog, Ui_Dialog):
    def __init__(self, Ulist = None,parent = None):
        super().__init__(parent)
        
        self.currlist = Ulist
        
        self.setupUi(self)
        
        self.back_btn.clicked.connect(lambda: self.close())
        self.update_btn.clicked.connect(self.init_update_user)
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        
        self.FName_LE.setText(self.currlist[4])
        self.LName_LE.setText(self.currlist[5])
        self.UName_LE.setText(self.currlist[2])
        self.ULevel_CB.setCurrentIndex(int(self.currlist[1]))
        self.Email_LE.setText(self.currlist[8])
        self.BDate_DE.setDate(self.currlist[11])
        self.Sex_CB.setCurrentIndex(int(self.currlist[6]))
        self.Phono_LE.setText(self.currlist[7])
        self.Pos_LE.setText(self.currlist[9])
        self.DHired_DE.setDate(self.currlist[10])
        self.Address_LE.setText(self.currlist[12])
        
    def init_update_user(self):
        
        self.confirmed_update()
        
        pass
    
    def confirmed_update(self):
        
        oldUlist = [self.currlist[2], self.currlist[4], self.currlist[5]]
        newUlist = [self.ULevel_CB.currentIndex() ,self.UName_LE.text(),
                        self.FName_LE.text(), self.LName_LE.text(),
                        self.Sex_CB.currentIndex(), self.Phono_LE.text(),
                        self.Email_LE.text(), self.Pos_LE.text().replace('+', '', 1),
                        self.DHired_DE.date().toPyDate(), self.BDate_DE.date().toPyDate(),
                        self.Address_LE.text()]
        
        currdb = dbcont('admin', 123456)
        
        currdb.update_user_protocol(oldUlist, newUlist)
        
        
        Dlg =  DLG_Alert()
        Dlg.exec()