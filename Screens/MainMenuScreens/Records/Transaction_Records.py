import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QTableWidgetItem
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream
from PyQt5 import QtCore


from .Transaction_Records_ui import Ui_MainWindow

from .Dialog.DLog_Receipt_Reprint import DLG_Receipt_Reprint

from Database.DBController import dbcont

class Trans_Rec_Window(QMainWindow, Ui_MainWindow):

    Add_btnsgl = QtCore.pyqtSignal()
    back_btnsgl = QtCore.pyqtSignal()
    
    db = dbcont()
    
    def __init__(self):
        super(Trans_Rec_Window,self).__init__()
        self.setupUi(self)
        self.set_tableElements()
        
        
        self.Receipts_Table.setColumnWidth(0,150)
        self.Receipts_Table.setColumnWidth(1,150)
        self.Receipts_Table.setColumnWidth(2,200)
        self.Receipts_Table.setColumnWidth(3,150)
        self.Receipts_Table.setColumnWidth(4,200)
        self.Receipts_Table.setColumnWidth(5,200)
        self.Receipts_Table.setColumnWidth(6,200)
        
        self.Back_btn.clicked.connect(lambda: self.back_btnsgl.emit())
        self.Refresh_btn.clicked.connect(self.set_tableElements)
        self.Search_btn.clicked.connect(self.search_tableElements)
        
        self.Receipts_Table.itemDoubleClicked.connect(self.show_receipt)
        
    def show_receipt(self, item):
        
        receipt = self.db.search_trans_receipts(searchstr= self.Receipts_Table.item(item.row(), 0).text())
        
        prodlist = self.db.get_receipt_products(ReceiptID= receipt[0])
        
        Receipt_Dlog = DLG_Receipt_Reprint(
                                prodlist= prodlist,
                                Tprice= receipt[3],
                                Ptype= receipt[5],
                                Pprice= receipt[4],
                                DTime= receipt[2],
                                RID= receipt[0],
                                GCRef= receipt[6]
                                )
        Receipt_Dlog.exec()
        
    def search_tableElements(self):
        self.Receipts_Table.setRowCount(0)
        result = self.db.search_trans_receipts(searchstr= self.search_LE.text())
        for row_number, row_data in enumerate(result):
            self.Receipts_Table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                if column_number == 5:
                        data = self.db.get_payment_type(id= data)
                if column_number == 2:
                        data = data.strftime('%B %d, %Y %H:%M')
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignCenter)
                self.Receipts_Table.setItem(row_number, column_number, item)
    
    def set_tableElements(self):
            self.Receipts_Table.setRowCount(0)
            result = self.db.get_all_trans_receipts()
            self.search_LE.clear()
            for row_number, row_data in enumerate(result):
                self.Receipts_Table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if column_number == 5:
                        data = self.db.get_payment_type(id= data)
                    if column_number == 2:
                        data = data.strftime('%B %d, %Y %H:%M')
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.Receipts_Table.setItem(row_number, column_number, item)