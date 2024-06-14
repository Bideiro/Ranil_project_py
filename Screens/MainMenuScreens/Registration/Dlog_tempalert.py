import sys
from PyQt5.QtWidgets import QMainWindow,QDialog, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream
from PyQt5.QtGui import QIntValidator

from .Registration_user_ui import Ui_MainWindow
from .DLog_tempalert_ui import Ui_Dialog

from Database.DBController import dbcont

from PyQt5 import QtWidgets, QtGui, QtCore


class DLGsucc(QDialog, Ui_Dialog):
    
    def __init__(self,parent = None):
        super().__init__(parent)
        
        self.setupUi(self)
        
        self.succ_btn.clicked.connect(self.close)
        