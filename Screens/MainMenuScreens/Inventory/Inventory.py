import sys
import os
import mysql.connector
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget, QTableWidgetItem, QTableWidget, QDialog
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream
from .Dlog_editprod_ui import Ui_Dialog
from .Inventory_ui import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore

class EditProductDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # You can initialize widgets and setup signals here if needed
        
        
class Inventory_Window(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super(Inventory_Window,self).__init__()
        self.setupUi(self)
        self.tableWidget.setColumnWidth(0,150)
        self.tableWidget.setColumnWidth(1,200)
        self.tableWidget.setColumnWidth(2,100)
        self.tableWidget.setColumnWidth(3,100)
        self.tableWidget.setColumnWidth(4,125)
        self.tableWidget.setColumnWidth(5,100)
        self.tableWidget.cellClicked.connect(self.on_cell_clicked)
        #Database setup 
        self.user = "user"
        self.passwd = "passwd"
        self.database = "ranil_proj"
        self.host = "localhost"  

    def on_refreshbtn_clicked(self):
        print('Beep!')
        result = self.get_Data()
        self.lineEdit.clear()
        if result:
            self.tableWidget.setRowCount(len(result))

            for row_number, row_data in enumerate(result):
                #self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        else: 
            print('Error')
            return
    #Search Function
    def search_func(self, search_term):
        mydb = mysql.connector.connect(
            host="localhost",
            user= "root",
            passwd= "password",
            database="ranil_proj"
        )

        mycursor = mydb.cursor()
        #SQL Statement to retrieve data
        searchcommand = """
                        SELECT ProductID, ProductName, SellingPrice, Stock, ExpirationDate FROM products
                        WHERE ProductID LIKE %s
                        OR ProductName LIKE %s
                        OR SellingPrice LIKE %s
                        OR ExpirationDate LIKE %s
                        OR StockStatus LIKE %s
                        """
        #LIKE clause
        like_search_term = '%' + search_term + '%'
        mycursor.execute(searchcommand, (like_search_term, like_search_term, like_search_term, like_search_term, like_search_term, like_search_term))
        #fetchall = get all
        searchResult = mycursor.fetchall()

        return searchResult
    #Function for getting data
    def get_Data(self):
        
        mydb = mysql.connector.connect(
            host="localhost",
            user= "root",
            passwd= "password",
            database="ranil_proj"
        )

        mycursor = mydb.cursor()
        #SQL Statement to retrieve data
        command = "SELECT * FROM products;"

        mycursor.execute(command)
        #fetchall = get all
        result = mycursor.fetchall()

        return result
    def on_testbtn_clicked(self):
        print('Search!')
        

        column = ["ProductID", "ProductName", "SellingPrice", "Quantity", "ExpirationDate", "StockStatus"]
        #Clear table
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(len(column))
        self.tableWidget.setHorizontalHeaderLabels(column)

        #Get search term from line edit
        searchTerm = self.lineEdit.text()

        #Search according to search term
        searchResult = self.search_func(searchTerm)

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

        
        