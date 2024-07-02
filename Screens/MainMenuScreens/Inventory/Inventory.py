from gc import isenabled
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialog
from PyQt5.QtCore import Qt
from Database.DBController import dbcont

from .Dialogs.DLog_UpdateProdDetails import DLG_Edit_Prod
from .Inventory_ui import Ui_MainWindow


class Inventory_Window(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super(Inventory_Window,self).__init__()
        self.setupUi(self)
        
        self.db = dbcont('admin', 123456)
        
        self.Product_Table.setColumnWidth(0,150)
        self.Product_Table.setColumnWidth(1,150)
        self.Product_Table.setColumnWidth(2,150)
        self.Product_Table.setColumnWidth(3,150)
        self.Product_Table.setColumnWidth(4,150)
        
        self.set_tableElements()
        
        self.Refresh_btn.clicked.connect(self.set_tableElements)
        self.Search_btn.clicked.connect(self.search)
        
        self.Product_Table.itemClicked.connect(self.clicked_item)

    def set_tableElements(self):
        self.Product_Table.setRowCount(0)
        result = []
        result = self.db.get_all_prod(inv=True)
        self.search_LE.clear()
        self.Product_Table.setRowCount(len(result))
        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):
                if column_number == 3:
                    data = self.db.get_unittype(id= data)
                    pass
                if column_number == 2:
                    data = self.db.get_cate(id= data)
                    pass
                if column_number == 8:
                    if data == 1:
                        data = 'Available'    
                    else:
                        data = 'Unavailable'
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignCenter)
                self.Product_Table.setItem(row_number, column_number, item)
    
    def search(self):
        self.Product_Table.setRowCount(0)
        searchResult = self.db.search_prod(self.search_LE.text(),inv= True)

        self.Product_Table.setRowCount(len(searchResult))
        if searchResult:
            self.Product_Table.setRowCount(len(searchResult))
            for row_number, row_data in enumerate(searchResult):
                self.Product_Table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if column_number == 3:
                        data = self.db.get_unittype(id= data)
                    if column_number == 2:
                        data = self.db.get_cate(id= data)
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
        Dlg = DLG_Edit_Prod(Plist= prod_values, isEnabled= self.db.get_status(RPID=prod_values[0]))
        Dlg.exec()
        if Dlg.result() == 1:
            self.newPlist = [self.db._create_rid(RID= prod_values[0],typeID=Dlg.Cat_CB.currentIndex(),prod=True),
                        Dlg.PName_LE.text(),Dlg.SPrice_LE.text(),
                        Dlg.Desc_LE.text(),Dlg.Unit_CB.currentIndex(),
                        Dlg.Cat_CB.currentIndex()]
            oldPlist = [prod_values[0]]
            self.db.update_prod_protocol(RPID=oldPlist, NewPlist = self.newPlist)
        self.set_tableElements()
        
