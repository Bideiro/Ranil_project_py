import datetime
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget, QTableWidgetItem,  QTableWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream
from Database.DBController import dbcont
from .Sales_ui import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
class Sales_Window(QMainWindow, Ui_MainWindow):
    
    db = dbcont()
    
    def __init__(self):
        super(Sales_Window,self).__init__()
        self.setupUi(self)

        self.Sales_Table.setColumnWidth(0,200)
        self.Sales_Table.setColumnWidth(1,200)
        self.Sales_Table.setColumnWidth(2,150)
        self.Sales_Table.setColumnWidth(3,150)
        self.Sales_Table.setColumnWidth(4,150)
        self.Sales_Table.setColumnWidth(5,250)
        self.Sales_Table.setColumnWidth(6,200)
        self.set_tableElements()
        
        self.Refresh_btn.clicked.connect(self.set_tableElements)
        self.Search_btn.clicked.connect(self.search)
        self.annualSalesbtn.clicked.connect(self.changeTableYearly)
        self.dailySalesbtn.clicked.connect(self.set_tableElements)
        self.monthlySalesbtn.clicked.connect(self.changeTableMonthly)
        self.comboBox.setVisible(False)
        
        
    def set_tableElements(self):
        
        for x in range(self.Sales_Table.columnCount()):
            self.Sales_Table.removeColumn(x)
            
        self.Sales_Table.setColumnCount(6)
            
        self.Sales_Table.setHorizontalHeaderLabels(['Date / Time', 'Reference Number' , 'User' , 'Total Price' , 'GCash Reference Number' , 'Payment Type'])
        
        self.Sales_Table.setColumnWidth(0,200)
        self.Sales_Table.setColumnWidth(1,200)
        self.Sales_Table.setColumnWidth(2,150)
        self.Sales_Table.setColumnWidth(3,150)
        self.Sales_Table.setColumnWidth(4,150)
        self.Sales_Table.setColumnWidth(5,250)
        self.Sales_Table.setColumnWidth(6,200)
        
        result = self.db.get_all_sales()
        self.search_LE.clear()
        self.Sales_Table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.Sales_Table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                if column_number == 5 :
                    data = self.db.get_payment_type(id= data)
                if column_number == 0:
                    data = data.strftime('%B %d, %Y %H:%M')
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignCenter)
                self.Sales_Table.setItem(row_number, column_number, item)
        
    def search(self):
        
        for x in range(self.Sales_Table.columnCount()):
            self.Sales_Table.removeColumn(x)
        
        self.Sales_Table.setColumnCount(6)
        
        self.Sales_Table.setHorizontalHeaderLabels(['Date / Time', 'Reference Number' , 'User' , 'Total Price' , 'GCash Reference Number' , 'Payment Type'])
        
        self.Sales_Table.setColumnWidth(0,200)
        self.Sales_Table.setColumnWidth(1,200)
        self.Sales_Table.setColumnWidth(2,150)
        self.Sales_Table.setColumnWidth(3,150)
        self.Sales_Table.setColumnWidth(4,150)
        self.Sales_Table.setColumnWidth(5,250)
        self.Sales_Table.setColumnWidth(6,200)
        
        searchResult = self.db.search_sales(self.search_LE.text())
        self.search_LE.clear()
        self.Sales_Table.setRowCount(0)
        if searchResult:
            for row_number, row_data in enumerate(searchResult):
                self.Sales_Table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if column_number == 6 :
                        data = self.db.get_payment_type(id= data)
                    if column_number == 0:
                        data = data.strftime('%B %d, %Y %H:%M')
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.Sales_Table.setItem(row_number, column_number, item)
        
    def changeTableYearly(self):
        
        for x in range(self.Sales_Table.columnCount()):
            self.Sales_Table.removeColumn(x)
        
        self.Sales_Table.setColumnCount(2)
            
        self.Sales_Table.setHorizontalHeaderLabels(['Annual', 'Total'])
        
        self.Sales_Table.setColumnWidth(0,200)
        self.Sales_Table.setColumnWidth(1,200)
        
        Result = self.db.get_sales_report(yearly=True)
        self.Sales_Table.setRowCount(0)
        if Result:
            for row_number, row_data in enumerate(Result):
                self.Sales_Table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.Sales_Table.setItem(row_number, column_number, item)

    def changeTableMonthly(self):
        
        for x in range(self.Sales_Table.columnCount()):
            self.Sales_Table.removeColumn(x)
            
        self.Sales_Table.setColumnCount(2)
            
        self.Sales_Table.setHorizontalHeaderLabels(['Monthly', 'Total'])
        
        self.Sales_Table.setColumnWidth(0,200)
        self.Sales_Table.setColumnWidth(1,200)
        
        Result = self.db.get_sales_report(monthly=True)
        self.Sales_Table.setRowCount(0)
        if Result:
            for row_number, row_data in enumerate(Result):
                self.Sales_Table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if column_number == 0:
                        date_time = datetime.datetime(1900, data, 1)
                        data = date_time.strftime('%B')
                    
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.Sales_Table.setItem(row_number, column_number, item)