import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .Records_1_ui import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
class Records_1_Window(QMainWindow, Ui_MainWindow):

    trans_btnsgl = QtCore.pyqtSignal()
    receipt_btnsgl = QtCore.pyqtSignal()
    
    def __init__(self):
        super(Records_1_Window,self).__init__()
        self.setupUi(self)
        
        
        self.trans_btn.clicked.connect(self.to_trans)
        self.receipts_btn.clicked.connect(self.to_receipt)
        
    def to_trans(self):
        self.inven_btnsgl.emit()
        
    def to_receipt(self):
        self.sales_btnsgl.emit()