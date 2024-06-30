import sys
from PyQt5.QtWidgets import QMainWindow,QDialog, QPushButton, QWidget
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import Qt

from .DLog_PaymentCombined_ui import Ui_Dialog
from Dialogs.DLog_Alert import DLG_Alert

class DLG_SplitPayment(QDialog, Ui_Dialog):
    
    def __init__(self, price, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.Popup)
        
        self.price = price
        
        self.onlyInt = QIntValidator()
        self.Input_LE.setValidator(self.onlyInt)
        
        self.ok_btn.clicked.connect(self.confirmed)
        
    def confirmed(self):
        if self.Input_LE.text() =='':
            Dlg = DLG_Alert(msg='Cash amount is empty!')
            Dlg.exec()
        elif self.Input3_LE.text() =='':
            Dlg = DLG_Alert(msg='GCash amount is empty!')
            Dlg.exec()
        elif self.Input2_LE.text() =='':
            Dlg = DLG_Alert(msg='GCash Reference is empty!')
            Dlg.exec()
        elif (int(self.Input3_LE.text()) + int(self.Input_LE.text())) < self.price:
            Dlg = DLG_Alert(msg= 'Insufficient cash!')
            Dlg.exec()
        elif (int(self.Input3_LE.text()) + int(self.Input_LE.text())) > self.price:
            change = (int(self.Input3_LE.text()) + int(self.Input_LE.text())) - self.price
            Dlg = DLG_Alert(msg= f'Transaction succesfull! (Change is {str(change)})')
            self.done(1)
            Dlg.exec()
        else: 
            Dlg = DLG_Alert(msg= 'Transaction succesfull!')
            Dlg.exec()
            self.done(1)