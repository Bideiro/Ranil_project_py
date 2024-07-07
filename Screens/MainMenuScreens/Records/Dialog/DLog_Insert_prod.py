
from PyQt5.QtWidgets import QMainWindow,QDialog, QPushButton, QWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream


from .DLog_Insert_prod_ui import Ui_Dialog
from .DLog_Receipt_Product_Details import DLG_Receipt_Product_Details
from Dialogs.DLog_Alert import DLG_Alert
from Database.DBController import dbcont
from Database.App_functions import check_prod_validity

class DLG_Insert_Prod(QDialog, Ui_Dialog):
    
    db = dbcont()
    
    selRPID = None
    selPrice = None
    selAmount = None
    selEdate = None
    RPIDList = None
    ProdDetails = None
    
    def __init__(self,parent = None, RPIDlist = None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.RPIDList = RPIDlist
        self.setWindowFlags(Qt.Popup)
        self.set_table_elements()
        
        self.Product_Table.itemClicked.connect(self.set_item)
        
        self.Search_btn.clicked.connect(self.search)
        self.Clear_btn.clicked.connect(self.refresh)
        self.Cancel_btn.clicked.connect(lambda: self.done(0))
        self.Confirm_btn.clicked.connect(self.confirmed)
        
        
    def confirmed(self):
        if self.selRPID == None:
            Dlg = DLG_Alert(msg='No Selected Product!')
            Dlg.exec()
            
        elif self.selRPID in self.RPIDList:
            Dlg = DLG_Alert(msg='Product Already in list!')
            Dlg.exec()
            
        else:
            Dlg_amount = DLG_Receipt_Product_Details()
            Dlg_amount.exec()
            
            if Dlg_amount.result() == 1:
                self.selAmount = Dlg_amount.PQuantity_LE.text()
                self.selPrice = Dlg_amount.PBought_LE.text()
                self.selEdate = str(Dlg_amount.EDate_DE.date().toPyDate())
                self.done(1)
                Dlg = DLG_Alert(msg= 'Item Added!')
                Dlg.exec()
            else:
                Dlg = DLG_Alert(msg='Enter an amount to add to reciept!')
                Dlg.exec()

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
        self.selRPID = prod_values[0]

    def refresh(self):
        self.search_LE.clear()
        self.set_table_elements()
    
    def set_table_elements(self):
        self.Product_Table.setRowCount(0)
        result = self.db.get_all_prod(records=True)
        for row_number, row_data in enumerate(result):
            self.Product_Table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                if column_number == 3:
                    data = self.db.get_unittype(id= data)
                if column_number == 2:
                    data = self.db.get_cate(id= data)
                self.Product_Table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    
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
                    self.Product_Table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        else:
            print('Error')
            return