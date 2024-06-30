import sys
from PyQt5.QtWidgets import QMainWindow,QDialog, QPushButton, QWidget
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import Qt

from .DLog_GCash_ui import Ui_Dialog
from Dialogs.DLog_Alert import DLG_Alert

class DLG_GCash(QDialog, Ui_Dialog):
    
    def __init__(self, price, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.Popup)
        
        self.price = price
        
        self.onlyInt = QIntValidator()
        self.Input_LE.setValidator(self.onlyInt)
        
        self.ok_btn.clicked.connect(self.confirmed)
        
    def confirmed(self):
        if int(self.Input_LE.text()) < self.price:
            Dlg = DLG_Alert(msg= 'Insufficient cash!')
            Dlg.exec()
            
        elif self.Input2_LE.text() == '':
            Dlg = DLG_Alert(msg= 'No GCash reference number!')
            Dlg.exec()
            
        elif int(self.Input_LE.text()) > self.price:
            change = int(self.Input_LE.text()) - self.price
            Dlg = DLG_Alert(msg= f'Transaction succesfull! (Change is {str(change)})')
            Dlg.exec()
            
        else:
            Dlg = DLG_Alert(msg= 'Transaction succesfull!')
            Dlg.exec()
            self.done(1)