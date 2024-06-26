import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .Add_Receipt_ui import Ui_MainWindow
from .Dialog.DLog_Insert_prod import DLG_Insert_Prod
from Database.DBController import dbcont

from PyQt5 import QtWidgets, QtGui, QtCore
class add_reciept_Window(QMainWindow, Ui_MainWindow):

    Add_btnsgl = QtCore.pyqtSignal()
    
    TableRPID = set()
    
    selectedprods = None
    
    def __init__(self):
        super(add_reciept_Window,self).__init__()
        self.setupUi(self)
        self.db = dbcont('admin', 123456)
        
        
        self.AProduct_btn.clicked.connect(self.Dlg_add_prod)
        self.Finish_btn.clicked.connect(self.init_add_receipt)
    
    def init_add_receipt(self):
        
        
        pass
    
    def Dlg_add_prod(self):
        
        Dlg = DLG_Insert_Prod(RPIDlist= self.TableRPID)
        Dlg.exec()
        if Dlg.result() == 1:
            selprod = self.db.search_prod(searchstr=Dlg.selRPID, receipt=True)
            self.TableRPID.add(selprod[0])
            rowpos = self.Products_Table.rowCount()
            self.Products_Table.insertRow(rowpos)
            for col, data in enumerate(selprod):
                    self.Products_Table.setItem(rowpos, col, QTableWidgetItem(str(data)))
            self.Products_Table.setItem(rowpos, 2, QTableWidgetItem(Dlg.selPrice))
            self.Products_Table.setItem(rowpos, 3, QTableWidgetItem(Dlg.selAmount))
        else:
            print('cancelled')