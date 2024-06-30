import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .User_Logs_ui import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
class User_Logs_Window(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super(User_Logs_Window,self).__init__()
        self.setupUi(self)
        
        
