import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .MainMenu_ui import Ui_MainWindow
from .MainMenuScreens.testtest import TestWindow
from Database.DBController import dbcont
from PyQt5 import QtWidgets, QtGui, QtCore
class MainMenuWindow( QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super(MainMenuWindow,self).__init__()
        self.setupUi(self)
        
        
        self.tetest = TestWindow()
        
        
        self.stackedWidget.addWidget(self.tetest)
        self.stackedWidget.setCurrentWidget(self.tetest)
        
    @pyqtSlot()
    # Functions changing windows
    def on_login_btn_clicked(self):
        print("Login Attempt")
        
        db = dbcont(self.userLE.text(),self.passwordLE.text())
        db.conn()
        
    # @pyqtSlot()
    # def on_forgotpass_btn_clicked(self):
    #     print("forgot")
    #     self.forgot.emit()
        