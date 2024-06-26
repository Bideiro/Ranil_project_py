
from PyQt5.QtWidgets import QMainWindow,QDialog, QPushButton, QWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream
from PyQt5 import QtWidgets, QtGui, QtCore

from .DLog_Insert_prod_ui import Ui_Dialog
from Dialogs.DLog_Alert import DLG_Alert
from Database.DBController import dbcont
from Database.App_functions import check_prod_validity

class DLG_Insert_Prod(QDialog, Ui_Dialog):
    
    selprod = []
    
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.db = dbcont('admin',123456)
        
        self.set_table_elements()
        
        self.Product_Table.itemClicked.connect(self.set_item)
        
        self.Search_btn.clicked.connect(self.search)
        self.Clear_btn.clicked.connect(self.set_table_elements)
        self.Cancel_btn.clicked.connect(lambda: self.done(0))
        self.Confirm_btn.clicked.connect(self.confirmed)
        
        
    def confirmed(self):
        
        
        pass
    
    def set_table_elements(self):
        result = self.db.get_all_prod(inv=True)
        self.Product_Table.setRowCount(len(result))
        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):

                if column_number == 6:
                    data = self.db.get_id_value(id= data, unit= True)
                if column_number == 7:
                    data = self.db.get_id_value(id= data, cate= True)
                self.Product_Table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
    
    def set_item(self,item):
        row = item.row()
        column_count = self.Product_Table.columnCount()
        prod_values = []
        
        for column in range(column_count):
            cell_item = self.Product_Table.item(row, column)
            if cell_item is not None:
                prod_values.append(cell_item.text())
            else:
                prod_values.append('')
        self.selprod = prod_values
        print(self.selprod)
    
    def search(self):
        self.Product_Table.setRowCount(0)
        
        searchResult = self.db.search_prod(self.search_LE.text(),inv= True)

        #Set number of rows to match search results
        self.Product_Table.setRowCount(len(searchResult))
        #Populate table with search result
        if searchResult:
            self.Product_Table.setRowCount(len(searchResult))
            print(len(searchResult))
            print(searchResult)
            for row_number, row_data in enumerate(searchResult):
                self.Product_Table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if column_number == 6:
                        data = self.db.get_id_value(id= data, unit= True)
                    if column_number == 7:
                        data = self.db.get_id_value(id= data, cate= True)
                    self.Product_Table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        else:
            print('Error')
            return