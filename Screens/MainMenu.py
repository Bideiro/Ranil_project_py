import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .MainMenu_ui import Ui_MainWindow
from .MainMenuScreens.About import AboutWindow

from Database.DBController import dbcont
from PyQt5 import QtWidgets, QtGui, QtCore
class MainMenuWindow( QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super(MainMenuWindow,self).__init__()
        self.setupUi(self)
        
        # Initializing Screens
        
        self.about = AboutWindow()
        
        # Adding Widgets into stack
        
        self.stackedWidget.addWidget(self.about)
        
        
        
        # self.stackedWidget.addWidget(self.tetest)
        # self.stackedWidget.setCurrentWidget(self.tetest)
        
    @pyqtSlot()
    # Functions changing windows
    def on_about_sdbtn_clicked(self):
        self.stackedWidget.setCurrentWidget(self.about)
        
    # @pyqtSlot()
    # def on_forgotpass_btn_clicked(self):
    #     print("forgot")
    #     self.forgot.emit()
        