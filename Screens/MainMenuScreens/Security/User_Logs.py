import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QTableWidgetItem
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .User_Logs_ui import Ui_MainWindow
from Database.DBController import dbcont
from PyQt5 import QtWidgets, QtGui, QtCore
class User_Logs_Window(QMainWindow, Ui_MainWindow):
    
    db = dbcont()
    
    def __init__(self):
        super(User_Logs_Window,self).__init__()
        self.setupUi(self)
        self.set_tableElements()
        
        self.Log_Table.setColumnWidth(0,150)
        self.Log_Table.setColumnWidth(1,150)
        self.Log_Table.setColumnWidth(2,150)
        self.Log_Table.setColumnWidth(3,150)
        self.Log_Table.setColumnWidth(4,200)
        
        
    def set_tableElements(self):
            self.Log_Table.setRowCount(0)
            result = []
            result = self.db.get_logs()
            self.Log_Table.setRowCount(len(result))
            for row_number, row_data in enumerate(result):
                for column_number, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.Log_Table.setItem(row_number, column_number, item)