import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .Home_ui import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
class HomeWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(HomeWindow,self).__init__()
        self.setupUi(self)