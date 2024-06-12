import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .testtest_ui import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
class TestWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(TestWindow,self).__init__()
        self.setupUi(self)