from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialog
from PyQt5 import QtCore

from Database.DBController import dbcont

from .Transaction_Payment_ui import Ui_MainWindow
from Dialogs.DLog_Alert import DLG_Alert

class Payment_Window(QMainWindow, Ui_MainWindow):
    
    cancel_btnsgl = QtCore.pyqtSignal()
    db = dbcont()
    
    def __init__(self,SProdList = None):
        super(Payment_Window,self).__init__()
        self.prodlist = None
        self.setupUi(self)
        
        if SProdList == None:
            self.prodlist = []
        else:
            self.prodlist = SProdList
        
        self.Home_btn.clicked.connect(lambda: print(self.prodlist))
        self.Cash_btn.clicked.connect(self.set_table_elements)
        self.Cancel_btn.clicked.connect(self.clean_screen)
        self.CDiscount_btn.clicked.connect(self.set_totalprice)
        
    def clean_screen(self):
        self.Product_Table.setRowCount(0)
        self.TPrice_L.setText('0')
        self.Discount_LE.setText('0')
        self.prev_window()
        
    def prev_window(self):
        self.cancel_btnsgl.emit()

    def init_screen(self):
        self.set_totalprice()
        self.set_table_elements()
        print(self.prodlist)
    
    def set_totalprice(self):
        totalprice = 0
        for prod in self.prodlist:
            totalprice += self.db.prod_price(id= prod[0]) * int(prod[2])
            
        if self.Discount_LE.text() != '' :
            dc = int(self.Discount_LE.text())
            if 0 <= dc and dc <= 100:
                totalprice -= (int(totalprice) * (int(self.Discount_LE.text())/100))
                self.TPrice_L.setText(str(totalprice))
            else:
                Dlg = DLG_Alert(msg= 'Ranging from 0 - 100 Only!')
                Dlg.exec()
        else:
            self.TPrice_L.setText(str(totalprice))
        
    def set_table_elements(self):
        self.Product_Table.setRowCount(len(self.prodlist))
        for row_number, row_data in enumerate(self.prodlist):
            for column_number, data in enumerate(row_data):
                self.Product_Table.setItem(row_number, column_number, QTableWidgetItem(str(data)))