import sys
from PyQt5.QtWidgets import QMainWindow,QDialog, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .DLog_NewUnit_ui import Ui_Dialog
from Dialogs.DLog_Alert import DLG_Alert

class DLG_NUnit(QDialog, Ui_Dialog):
    
    def __init__(self,parent = None):
        super().__init__(parent)
        
        self.setupUi(self)
        self.back_btn.clicked.connect(self.cancelled)
        self.ok_btn.clicked.connect(self.confirmed)
        self.setWindowFlags(Qt.Popup)

    def cancelled(self):
        self.done(0)

    def confirmed(self):
        if self.Input_LE.text() == '':
            Dlg = DLG_Alert(msg= 'Empty Unit input!')
            Dlg.exec()
        else:
            self.done(1)