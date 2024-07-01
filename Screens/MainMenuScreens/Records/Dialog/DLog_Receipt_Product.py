import sys
from PyQt5.QtWidgets import QMainWindow,QDialog, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .DLog_Receipt_Product_ui import Ui_Dialog

from Dialogs.DLog_Alert import DLG_Alert
class DLG_Receipt_Product(QDialog, Ui_Dialog):
    
    def __init__(self,msg = None,msg2 = None, msg3 = None,parent = None):
        super().__init__(parent)
        
        self.setupUi(self)
        
        if msg == None and msg2 == None:
            self.alertmsg = 'Input:'
            self.alertmsg2 = 'Input:'
        else:
            self.alertmsg = msg
            self.alertmsg2 = msg2
            self.alertmsg3 = msg3
        self.label.setText(self.alertmsg)
        self.label2.setText(self.alertmsg2)
        self.label3.setText(self.alertmsg3)
        self.Confirm_btn.clicked.connect(self.confirm)
        # self.setWindowFlags(Qt.Popup)
        
    def confirm(self):
        if self.Input_LE.text() == '':
            Dlg = DLG_Alert(msg='Empty Amount Field!')
            Dlg.exec()
        elif self.Input2_LE.text() == '':
            Dlg = DLG_Alert(msg='Empty Product price Field!')
            Dlg.exec()
        
        else:
            self.done(1)