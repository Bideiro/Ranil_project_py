import sys
import os
import mysql.connector
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget, QTableWidgetItem, QTableWidget, QDialog

from Database.DBController import dbcont

from .Dlog_editprod_ui import Ui_Dialog
from .Inventory_ui import Ui_MainWindow


class EditProductDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
class Inventory_Window(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super(Inventory_Window,self).__init__()
        self.setupUi(self)
        
        self.db = dbcont('admin', 123456)
        
        # self.tableWidget.setColumnWidth(0,150)
        # self.tableWidget.setColumnWidth(1,200)
        # self.tableWidget.setColumnWidth(2,100)
        # self.tableWidget.setColumnWidth(3,1000)
        # self.tableWidget.setColumnWidth(4,125)
        # self.tableWidget.setColumnWidth(5,100)
        
        self.set_tableElements()
        
        self.Refresh_btn.clicked.connect(self.set_tableElements)
        self.Search_btn.clicked.connect(self.search)
        
        self.tableWidget.cellClicked.connect(self.on_cell_clicked)

    def set_tableElements(self):
        result = self.db.get_all_prod()
        self.search_LE.clear()
        self.tableWidget.setRowCount(len(result))
        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    #Function for getting data
    def get_Data(self):
        result = self.db.get_all_prod()
        return result
    
    def search(self):
        self.tableWidget.clear()
        searchResult = self.db.search_prod(self.search_LE.text())

        #Set number of rows to match search results
        self.tableWidget.setRowCount(len(searchResult))

        #Populate table with search result
        if searchResult:
            self.tableWidget.setRowCount(len(searchResult))
            for row_number, row_data in enumerate(searchResult):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        else: 
            print('Error')
            return
        
    def on_cell_clicked(self, row, column):
        item = self.tableWidget.item(row, column)
        if item is not None:
            # Instantiate and show your custom dialog
            dialog = EditProductDialog()
            dialog.exec_()