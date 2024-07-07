from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QDate

from Database.DBController import dbcont

from .Add_Receipt_ui import Ui_MainWindow

from .Dialog.DLog_Insert_prod import DLG_Insert_Prod
from Dialogs.DLog_Alert import DLG_Alert


from PyQt5 import QtCore
class add_reciept_Window(QMainWindow, Ui_MainWindow):

    Add_btnsgl = QtCore.pyqtSignal()
    Finish_btnsgl = QtCore.pyqtSignal()
    Back_btnsgl = QtCore.pyqtSignal()
    
    db = dbcont()
    RPIDList= set()
    Plist = []
    Dlg = None
    
    selectedprodRPID = None
    
    def __init__(self):
        super(add_reciept_Window,self).__init__()
        self.setupUi(self)
        
        self.DDate_DE.setDate(QDate.currentDate())
        self.ODate_DE.setDate(QDate.currentDate())
        
        self.AProduct_btn.clicked.connect(self.add_prod)
        self.RProduct_btn.clicked.connect(self.prod_removed)
        self.Finish_btn.clicked.connect(self.init_add_receipt)
        self.Back_btn.clicked.connect(self.prev_window)
        self.Products_Table.itemClicked.connect(self.select_prod)
    
    def select_prod(self):
        self.selectedprodRPID = self.Products_Table.item(self.Products_Table.currentRow(), 0).text()
    
    def prod_removed(self):
        if self.selectedprodRPID:
            self.RPIDList.remove(self.selectedprodRPID)
            for i, row in enumerate(self.Plist):
                if self.selectedprodRPID in row:
                    self.Plist.pop(i)
            self.selectedprodRPID = None
            self.refresh_table()
        else:
            Dlg = DLG_Alert(msg= 'No Selected Product!')
            Dlg.exec()
    
    def init_add_receipt(self):
        if self.RNumber_LE != '':
            rows_list = []
            for row in range(self.Products_Table.rowCount()):
                row_data = []
                for column in range(self.Products_Table.columnCount()):
                    item = self.Products_Table.item(row, column)
                    row_data.append(item.text() if item is not None else '')
                rows_list.append(row_data)
                
            Total = 0
            for value in rows_list:
                Total += ( int(value[2]) * int(value[3]) )
                
            self.db.add_receipt(RefNo= self.RNumber_LE.text(), TPrice= Total,
                                ODate= self.ODate_DE.date().toPyDate(),DDate= self.DDate_DE.date().toPyDate(),
                                Plist= rows_list)
            self.clear_table()
            self.Finish_btnsgl.emit()
        else:
            Dlg = DLG_Alert(msg= 'No Supplier Receipt Number!')
            Dlg.exec()
        
    def add_prod(self):
        
        self.Dlg = DLG_Insert_Prod(RPIDlist= self.RPIDList)
        self.Dlg.exec()
        if self.Dlg.result() == 1:
            SPdetails = [self.Dlg.selRPID, 
                        self.db.search_prod(searchstr=self.Dlg.selRPID, receipt=True)[1],
                        self.Dlg.selPrice,
                        self.Dlg.selAmount,
                        self.Dlg.selEdate
                        ]
            self.RPIDList.add(self.Dlg.selRPID)
            self.Plist.append(SPdetails)
            self.refresh_table()
        else:
            print('cancelled')
    
    def refresh_table(self):
        self.Products_Table.setRowCount(0)
        for row_number, row_data in enumerate(self.Plist):
            self.Products_Table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignCenter)
                self.Products_Table.setItem(row_number, column_number, item)
    
    def prev_window(self):
        self.Back_btnsgl.emit()
        self.clear_table()
    
    def clear_table(self):
        self.TableRPID.clear()
        self.Products_Table.setRowCount(0)
        selectedprods = None