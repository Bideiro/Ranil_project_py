import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .Add_Receipt_ui import Ui_MainWindow
from .Dialog.DLog_Insert_prod import DLG_Insert_Prod
from Database.DBController import dbcont

from PyQt5 import QtWidgets, QtGui, QtCore
class add_reciept_Window(QMainWindow, Ui_MainWindow):

    Add_btnsgl = QtCore.pyqtSignal()
    Finish_btnsgl = QtCore.pyqtSignal()
    Back_btnsgl = QtCore.pyqtSignal()
    
    TableRPID = set()
    Dlg = None
    
    selectedprods = None
    
    def __init__(self):
        super(add_reciept_Window,self).__init__()
        self.setupUi(self)
        self.db = dbcont('admin', 123456)
        
        self.AProduct_btn.clicked.connect(self.Dlg_add_prod)
        self.Finish_btn.clicked.connect(self.init_add_receipt)
        self.Back_btn.clicked.connect(self.prev_window)
    
    def init_add_receipt(self):
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
        
    def Dlg_add_prod(self):
        
        self.Dlg = DLG_Insert_Prod(RPIDlist= self.TableRPID)
        self.Dlg.exec()
        if self.Dlg.result() == 1:
            selprod = self.db.search_prod(searchstr=self.Dlg.selRPID, receipt=True)
            self.TableRPID.add(selprod[0])
            rowpos = self.Products_Table.rowCount()
            self.Products_Table.insertRow(rowpos)
            for col, data in enumerate(selprod):
                    self.Products_Table.setItem(rowpos, col, QTableWidgetItem(str(data)))
            self.Products_Table.setItem(rowpos, 2, QTableWidgetItem(self.Dlg.selPrice))
            self.Products_Table.setItem(rowpos, 3, QTableWidgetItem(self.Dlg.selAmount))
            self.Products_Table.setItem(rowpos, 4, QTableWidgetItem(self.Dlg.selEdate))
        else:
            print('cancelled')
    
    def prev_window(self):
        self.Back_btnsgl.emit()
        self.clear_table()
            
    def clear_table(self):
        self.TableRPID.clear()
        self.Products_Table.setRowCount(0)
        selectedprods = None