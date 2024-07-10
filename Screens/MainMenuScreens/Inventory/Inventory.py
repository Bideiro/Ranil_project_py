from gc import isenabled
from math import prod
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialog
from PyQt5.QtCore import Qt
from Database.DBController import dbcont

from .Dialogs.DLog_UpdateProdDetails import DLG_Edit_Prod
from .Inventory_ui import Ui_MainWindow


class Inventory_Window(QMainWindow, Ui_MainWindow):
    
    db = dbcont()
    
    def __init__(self):
        super(Inventory_Window,self).__init__()
        self.setupUi(self)
        
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
        # self.db.set_dynamic_expdate(refresh=True)
        self.Product_Table.setRowCount(0)
        result = []
        result = self.db.get_all_prod(inv=True)
        self.search_LE.clear()
        for row_number, row_data in enumerate(result):
            self.Product_Table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                if column_number == 3:
                    data = self.db.get_unittype(id= data)
                if column_number == 2:
                    data = self.db.get_cate(id= data)
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
        if searchResult:
            for row_number, row_data in enumerate(searchResult):
                self.Product_Table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if column_number == 3:
                        data = self.db.get_unittype(id= data)
                    if column_number == 2:
                        data = self.db.get_cate(id= data)
                    
                    if column_number == 8:
                        if data == 1:
                            data = 'Available'
                        else:
                            data = 'Unavailable'
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.Product_Table.setItem(row_number, column_number, item)
        else:
            print('Error')
            return
        
    def clicked_item(self, item):
        row = item.row()    
        prod_rid = self.Product_Table.item(row, 0).text()
        
        Dlg = DLG_Edit_Prod(Plist= self.db.search_prod(searchstr= prod_rid, inv= True)[0], isEnabled= self.db.access_status_prod(RPID=prod_rid))
        Dlg.exec()
        if Dlg.result() == 1:
            self.newPlist = [self.db._create_rid(RID= prod_rid ,typeID=Dlg.Cat_CB.currentIndex(),prod=True),
                        Dlg.PName_LE.text(),Dlg.SPrice_LE.text(),
                        Dlg.Desc_LE.text(),Dlg.Unit_CB.currentIndex(),
                        Dlg.Cat_CB.currentIndex()]
            oldPlist = [prod_rid]
            self.db.update_prod_protocol(RPID=oldPlist, NewPlist = self.newPlist)
        self.set_tableElements()
        
