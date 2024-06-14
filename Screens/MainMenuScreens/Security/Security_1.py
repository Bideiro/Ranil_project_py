import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .Security_1_ui import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
class Security_1_Window(QMainWindow, Ui_MainWindow):
    
    UInfo_btnsgl = QtCore.pyqtSignal()
    ULogs_btnsgl = QtCore.pyqtSignal()
    
    def __init__(self):
        super(Security_1_Window,self).__init__()
        self.setupUi(self)
        
        self.UInfo_btn.clicked.connect(self.to_UInfo)
        self.ULogs_btn.clicked.connect(self.to_ULogs)
    
    def to_UInfo(self):
        self.UInfo_btnsgl.emit()
        
    def to_ULogs(self):
        self.ULogs_btnsgl.emit()