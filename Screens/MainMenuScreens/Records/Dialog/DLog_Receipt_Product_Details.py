import sys
from PyQt5.QtWidgets import QMainWindow,QDialog, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream
from PyQt5.QtGui import QIntValidator

from .DLog_Receipt_Product_Details_ui import Ui_Dialog

from Dialogs.DLog_Alert import DLG_Alert
class DLG_Receipt_Product_Details(QDialog, Ui_Dialog):
    
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.setupUi(self)
        
        self.onlyInt = QIntValidator()
        self.PQuantity_LE.setValidator(self.onlyInt)
        self.PBought_LE.setValidator(self.onlyInt)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.Confirm_btn.clicked.connect(self.confirm)
        self.Cancel_btn.clicked.connect(lambda: self.done(0))
        
    
        
        
    def confirm(self):
        
        if self.PQuantity_LE.text() == '':
            Dlg = DLG_Alert(msg='Empty Amount Field!')
            Dlg.exec()
        elif self.PBought_LE.text() == '':
            Dlg = DLG_Alert(msg='Empty Product price Field!')
            Dlg.exec()
        
        else:
            self.done(1)