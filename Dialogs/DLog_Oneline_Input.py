import sys
from PyQt5.QtWidgets import QMainWindow,QDialog, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from Dialogs.DLog_Oneline_Input_ui import Ui_Dialog

from Dialogs.DLog_Alert import DLG_Alert
class DLG_Oneline_Input(QDialog, Ui_Dialog):
    
    def __init__(self,msg,parent = None):
        super().__init__(parent)
        
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint) 
        self.label.setText(msg)
        self.Confirm_btn.clicked.connect(self.confirm)
        self.Cancel_btn.clicked.connect(lambda: self.done(0))
        
    def confirm(self):
        if self.Input_LE.text() == '':
            Dlg = DLG_Alert(msg='Empty Field!')
            Dlg.exec()
        else:
            self.done(1)