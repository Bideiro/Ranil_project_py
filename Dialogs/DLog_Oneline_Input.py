import sys
from PyQt5.QtWidgets import QMainWindow,QDialog, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from Dialogs.DLog_Oneline_Input_ui import Ui_Dialog

from Dialogs.DLog_Alert import DLG_Alert
class DLG_Oneline_Input(QDialog, Ui_Dialog):
    
    def __init__(self,msg = None,parent = None):
        super().__init__(parent)
        
        self.setupUi(self)
        if msg == None:
            self.alertmsg = 'Success'
        else:
            self.alertmsg = msg
        self.label.setText(self.alertmsg)
        self.Confirm_btn.clicked.connect(self.confirm)
        
        # self.setWindowFlags(Qt.Popup)
        
    def confirm(self):
        if self.Input_LE.text() == '':
            Dlg = DLG_Alert(msg='Empty Field!')
            Dlg.exec()
        else:
            self.done(1)