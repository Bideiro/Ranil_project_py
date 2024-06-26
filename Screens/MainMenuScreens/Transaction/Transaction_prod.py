import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialog

from Database.DBController import dbcont


from .Transaction_Prod_ui import Ui_MainWindow
from Dialogs.DLog_Alert import DLG_Alert
from PyQt5 import QtCore

class Trans_prod_Window(QMainWindow, Ui_MainWindow):
    
    Done_btnsgl = QtCore.pyqtSignal()
    
    Sprod = None
    StableRPID = set()
    SProdConfirmed = []
    SprodRow = None
    
    def __init__(self):
        super(Trans_prod_Window,self).__init__()
        self.setupUi(self)
        self.db = dbcont('admin', 123456)
        self.set_tableElements()
        self.Product_Table.itemClicked.connect(self.clicked_item_prod)
        self.SProducts_Table.itemClicked.connect(self.clicked_item_sprod)
        self.Add_btn.clicked.connect(self.add_quantity)
        self.RProduct_btn.clicked.connect(self.remove_sprod)
        self.AProduct_btn.clicked.connect(self.add_to_list)
        self.Done_btn.clicked.connect(self.confirmed_order)
        self.Search_btn.clicked.connect(self.search)
        self.Clear_btn.clicked.connect(lambda: self.SProducts_Table.clear())
        
    def search(self):
        self.Product_Table.setRowCount(0)
        searchResult = self.db.search_prod(self.Search_LE.text(), trans= True)
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
        
    def set_tableElements(self):
        result = self.db.get_all_prod(trans= True)
        self.Search_LE.clear()
        self.Product_Table.setRowCount(len(result))
        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):
                self.Product_Table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
    def current_prod_reset(self):
        self.PName_L.setText(None)
        self.RUID_L.setText(None)
        self.SPrice_L.setText(None)
        self.EDate_L.setText(None)
        self.Quantity_LE.setText(None)
        
    def clicked_item_prod(self, item):
        row = item.row()
        column_count = self.Product_Table.columnCount()
        prod_values = []
        
        for column in range(column_count):
            cell_item = self.Product_Table.item(row, column)
            if cell_item is not None:
                prod_values.append(cell_item.text())
            else:
                prod_values.append('')
                
        self.PName_L.setText(prod_values[1])
        self.RUID_L.setText(prod_values[0])
        self.SPrice_L.setText(prod_values[2])
        self.EDate_L.setText(prod_values[4])
        
        self.Sprod = [prod_values[0],prod_values[1],prod_values[2],prod_values[4]]
        print(self.Sprod)
        
    def clicked_item_sprod(self, item):
        Sprod = self.db.search_prod(searchstr= self.SProducts_Table.item(item.row(), 0).text() ,id=True)
        self.SprodRow = item.row()
        self.PName_L.setText(Sprod[1])
        self.RUID_L.setText(Sprod[0])
        self.SPrice_L.setText(str(Sprod[2]))
        self.EDate_L.setText(str(Sprod[4]))
        self.Quantity_LE.setText(self.SProducts_Table.item(item.row(), 2).text())
        
    def remove_sprod(self):
        if self.SprodRow != None:
            RPID_item = self.SProducts_Table.item(self.SprodRow, 0)
            self.StableRPID.discard(RPID_item.text())
            print(self.StableRPID)
            
            self.SProducts_Table.removeRow(self.SprodRow)
            self.SprodRow = None
            self.current_prod_reset()
        else:
            Dlg = DLG_Alert(msg='No Selected Product in order list!')
            Dlg.exec()
        
    def add_to_list(self):
        if self.Sprod:
            if self.Sprod[0] not in self.StableRPID:
                
                self.StableRPID.add(self.Sprod[0])
                
                rowpos = self.SProducts_Table.rowCount()
                self.SProducts_Table.insertRow(rowpos)
                
                for col, data in enumerate(self.Sprod):
                    if col == 2:
                        self.SProducts_Table.setItem(rowpos, col, QTableWidgetItem(str(0)))
                    elif col == 0 or col == 1:
                        self.SProducts_Table.setItem(rowpos, col, QTableWidgetItem(str(data)))
            else:
                Dlg = DLG_Alert(msg='Already in list!')
                Dlg.exec()
        else:
            Dlg = DLG_Alert(msg='No Selected Item!')
            Dlg.exec()
        
    def add_quantity(self):
        search_text = self.RUID_L.text()
        found_item = None
        for row in range(self.SProducts_Table.rowCount()):
            for col in range(self.SProducts_Table.columnCount()):
                item = self.SProducts_Table.item(row, col)
                if item is not None and item.text() == search_text:
                    found_item = item
                    break
            if found_item is not None:
                break
        
        if found_item is not None:
            row = found_item.row()
            self.SProducts_Table.setItem(row,2,QTableWidgetItem(self.Quantity_LE.text()))
        else:
            print(f"Item '{search_text}' not found.")

    def confirmed_order(self):
        for row in range(self.SProducts_Table.rowCount()):
            row_data = []
            for col in range(self.SProducts_Table.columnCount()):
                item = self.SProducts_Table.item(row, col)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append('')
            self.SProdConfirmed.append(row_data)
            
            print(self.SProdConfirmed)
        self.Done_btnsgl.emit()