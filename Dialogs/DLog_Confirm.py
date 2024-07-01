import sys
from PyQt5.QtWidgets import QMainWindow,QDialog, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .DLog_Confirm_ui import Ui_Dialog

class DLG_Confirm(QDialog, Ui_Dialog):
    
    def __init__(self,msg = None,parent = None):
        super().__init__(parent)
        
        self.setupUi(self)
        if msg == None:
            self.alertmsg = 'DO YOU WANT TO PROCEED?'
        else:
            self.alertmsg = msg
        self.label.setText(self.alertmsg)
        self.Confirm_btn.clicked.connect(lambda: self.done(1))
        self.setWindowFlags(Qt.Popup)
        
        
        