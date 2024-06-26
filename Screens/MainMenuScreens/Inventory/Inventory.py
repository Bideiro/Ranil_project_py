from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialog

from Database.DBController import dbcont

from .Dialogs.Dlog_UpdateProdDetails import DLG_Edit_Prod
from .Inventory_ui import Ui_MainWindow


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
        
        self.Product_Table.itemClicked.connect(self.clicked_item)

    def set_tableElements(self):
        result = self.db.get_all_prod(inv=True)
        self.search_LE.clear()
        self.Product_Table.setRowCount(len(result))
        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):

                if column_number == 6:
                    data = self.db.get_id_value(id= data, unit= True)
                if column_number == 7:
                    data = self.db.get_id_value(id= data, cate= True)
                self.Product_Table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    
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
        
    def clicked_item(self, item):
        row = item.row()
        column_count = self.Product_Table.columnCount()
        prod_values = []
        
        for column in range(column_count):
            cell_item = self.Product_Table.item(row, column)
            if cell_item is not None:
                prod_values.append(cell_item.text())
            else:
                prod_values.append('')
        Dlg = DLG_Edit_Prod(Plist= prod_values)
        Dlg.exec()
        if Dlg.result() == 1:
            print(prod_values[7])
            newPlist = [self.db._create_rid(id= self.db.get_id_value(value= Dlg.Cat_CB.currentIndex(),cate=True),prod=True), Dlg.PName_LE.text(),Dlg.SPrice_LE.text(),Dlg.Desc_LE.text(),Dlg.Unit_CB.currentIndex(),Dlg.Cat_CB.currentIndex()]
            oldPlist = [prod_values[0]]
            self.db.update_prod_protocol(oldPlist, newPlist)
        self.set_tableElements()
        
        
        