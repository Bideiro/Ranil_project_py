
from PyQt5.QtWidgets import QMainWindow,QDialog, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .DLog_UpdateUserDetails_ui import Ui_Dialog

class DLG_Edit_User(QDialog, Ui_Dialog):
    def __init__(self, Ulist = None,parent = None):
        super().__init__(parent)
        
        self.setupUi(self)
        
        self.back_btn.clicked.connect(lambda: self.close())
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        
        self.FName_LE.setText(Ulist[4])
        self.LName_LE.setText(Ulist[5])
        self.UName_LE.setText(Ulist[2])
        self.ULevel_CB.setCurrentIndex(int(Ulist[1]))
        self.Email_LE.setText(Ulist[8])
        self.BDate_DE.setDate(Ulist[11])
        self.Sex_CB.setCurrentIndex(int(Ulist[6]))
        self.Phono_LE.setText(Ulist[7])
        self.Pos_LE.setText(Ulist[9])
        self.DHired_DE.setDate(Ulist[10])
        self.Address_LE.setText(Ulist[12])
        