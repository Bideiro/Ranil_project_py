import sys
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIntValidator

from .Maintenance_1_ui import Ui_MainWindow
from Database.DBController import dbcont
from Database.User_Manager import UserMana
from PyQt5 import QtWidgets, QtGui, QtCore
class Maintenance_Window(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super(Maintenance_Window,self).__init__()
        self.setupUi(self)
        
    

    def showFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(self, "Select a SQL File", "", "SQL Files (*.sql);;All Files (*)", options=options)
        if fileName:
            self.label.setText(f"Selected file: {fileName}")
            self.restore_database( fileName)