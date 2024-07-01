import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QTableWidgetItem, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .Supplier_Records_ui import Ui_MainWindow
from Database.DBController import dbcont
from PyQt5 import QtWidgets, QtGui, QtCore
class Supp_Rec_Window(QMainWindow, Ui_MainWindow):

    Add_btnsgl = QtCore.pyqtSignal()
    back_btnsgl = QtCore.pyqtSignal()
    
    db = dbcont()
    
    def __init__(self):
        super(Supp_Rec_Window,self).__init__()
        self.setupUi(self)
        self.set_tableElements()
        
        self.Add_btn.clicked.connect(lambda: self.Add_btnsgl.emit())
        self.Refresh_btn.clicked.connect(self.set_tableElements)
        self.Back_btn.clicked.connect(lambda: self.back_btnsgl.emit())
        
    
    
    def set_tableElements(self):
            self.SReceipts_Table.setRowCount(0)
            result = []
            result = self.db.get_all_supp_receipts()
            self.search_LE.clear()
            self.SReceipts_Table.setRowCount(len(result))
            for row_number, row_data in enumerate(result):
                for column_number, data in enumerate(row_data):
                    self.SReceipts_Table.setItem(row_number, column_number, QTableWidgetItem(str(data)))