import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .Transaction_1_ui import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
class Transaction_1_Window(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Transaction_1_Window,self).__init__()
        self.setupUi(self)
        
        
        