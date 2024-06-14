import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .Sales_ui import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
class Sales_Window(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super(Sales_Window,self).__init__()
        self.setupUi(self)
        