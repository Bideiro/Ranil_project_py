import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .Records_1_ui import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
class Records_1_Window(QMainWindow, Ui_MainWindow):

    SReciepts_btnsgl = QtCore.pyqtSignal()
    TReceipts_btnsgl = QtCore.pyqtSignal()
    
    def __init__(self):
        super(Records_1_Window,self).__init__()
        self.setupUi(self)
        
        
        self.SReciepts_btn.clicked.connect(self.to_Supp_trans)
        self.TReceipts_btn.clicked.connect(self.to_Trans_receipt)
        
    def to_Supp_trans(self):
        print("trans")
        self.SReciepts_btnsgl.emit()
        
    def to_Trans_receipt(self):
        print("receipts")
        self.TReceipts_btnsgl.emit()