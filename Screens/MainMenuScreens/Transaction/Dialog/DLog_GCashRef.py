import sys
from PyQt5.QtWidgets import QMainWindow,QDialog, QPushButton, QWidget
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import Qt

from .DLog_GCashRef_ui import Ui_Dialog
from Dialogs.DLog_Alert import DLG_Alert

class DLG_GCashRef(QDialog, Ui_Dialog):
    
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.Popup)
        
        self.onlyInt = QIntValidator()
        self.Input_LE.setValidator(self.onlyInt)
        
        self.ok_btn.clicked.connect(self.confirmed)
        
    def confirmed(self):
        if self.Input_LE.text() == '':
            Dlg = DLG_Alert(msg= 'GCash Reference cant be empty')
            self.done(0)
            Dlg.exec()
        else:
            Dlg = DLG_Alert(msg= f'Transaction succesfull!')
            self.done(1)
            Dlg.exec()
        
            
            
            