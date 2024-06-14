import sys
from PyQt5.QtWidgets import QMainWindow,QDialog, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .Registration_user_ui import Ui_MainWindow
from .DLog_newuserpass_ui import Ui_Dialog
from PyQt5 import QtWidgets, QtGui, QtCore
class Registration_user_Window(QMainWindow, Ui_MainWindow):

    back_btnsgl = QtCore.pyqtSignal()
    
    def __init__(self):
        super(Registration_user_Window,self).__init__()
        self.setupUi(self)
        
        self.back_btn.clicked.connect(self.prev_window)
        self.save_btn.clicked.connect(self.init_reg_protocol)
        
    def prev_window(self):
        self.back_btnsgl.emit()
        
    def init_reg_protocol(self):
        
        fname = self.FName_LE.text()
        lname = self.LName_LE.text()
        uname = self.user_LE.text()
        email = self.email_LE.text()
        loa = self.level_CB.currentText()
        bday = self.Bday_DE.date().toPyDate()
        gender = self.gender_CB.currentText()
        pos = self.pos_LE.text()
        phono = self.Phono_LE.text()
        dhire = self.DHire_DE.date().toPyDate()
        print(dhire)
        dlg = DLGnewuserpass(self)
        dlg.exec()
        
        
class DLGnewuserpass(QDialog):
    
    def __init__(self,parent = None):
        super().__init__(parent)
        
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)