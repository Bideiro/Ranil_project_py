import sys
from PyQt5.QtWidgets import QMainWindow,QDialog, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .DLog_Alert_BtnLess_ui import Ui_Dialog

class DLG_Alert(QDialog, Ui_Dialog):
    
    def __init__(self,msg = None,parent = None):
        super().__init__(parent)
        
        self.setupUi(self)
        if msg == None:
            self.alertmsg = 'Success'
        else:
            self.alertmsg = msg
        self.label.setText(self.alertmsg)
        self.setWindowFlags(Qt.Popup)
        