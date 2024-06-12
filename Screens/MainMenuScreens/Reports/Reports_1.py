import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .Reports_1_ui import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
class Reports_1_Window(QMainWindow, Ui_MainWindow):

    inven_btnsgl = QtCore.pyqtSignal()
    sales_btnsgl = QtCore.pyqtSignal()
    
    def __init__(self):
        super(Reports_1_Window,self).__init__()
        self.setupUi(self)
        
        
        self.inven_btn.clicked.connect(self.to_inven)
        self.sales_btn.clicked.connect(self.to_sales)
        
    def to_inven(self):
        self.inven_btnsgl.emit()
        
    def to_sales(self):
        self.sales_btnsgl.emit()