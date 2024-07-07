import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .Reports_1_ui import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
class Reports_1_Window(QMainWindow, Ui_MainWindow):

    Inven_btnsgl = QtCore.pyqtSignal()
    Sales_btnsgl = QtCore.pyqtSignal()
    ULogs_btnsgl = QtCore.pyqtSignal()
    
    def __init__(self):
        super(Reports_1_Window,self).__init__()
        self.setupUi(self)
        
        self.Inven_btn.clicked.connect(lambda: self.Inven_btnsgl.emit())
        self.Sales_btn.clicked.connect(lambda: self.Sales_btnsgl.emit())
        self.Ulogs_btn.clicked.connect(lambda: self.ULogs_btnsgl.emit())