import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream, pyqtSignal

from .ForgotPass_UI import Ui_MainWindow
from PyQt5 import QtCore

class ForgotPassWindow(QMainWindow, Ui_MainWindow):
    
    back = QtCore.pyqtSignal()
    
    def __init__(self):
        super(ForgotPassWindow,self).__init__()
        self.setupUi(self)
        
    @pyqtSlot()
    # initiate login
    def on_pushButton_clicked(self):
        print("back butn")
        self.back.emit()
        