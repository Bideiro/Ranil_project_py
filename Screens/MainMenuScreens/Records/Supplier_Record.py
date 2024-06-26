import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .Supplier_Records_ui import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
class Supp_Rec_Window(QMainWindow, Ui_MainWindow):

    Add_btnsgl = QtCore.pyqtSignal()
    
    def __init__(self):
        super(Supp_Rec_Window,self).__init__()
        self.setupUi(self)
        
        
        
        self.Add_btn.clicked.connect(lambda: self.Add_btnsgl.emit())
    