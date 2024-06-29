from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialog
from PyQt5 import QtCore
from PyQt5.QtGui import QIntValidator


from Database.DBController import dbcont

from Dialogs.DLog_Alert import DLG_Alert

from .Transaction_Payment_ui import Ui_MainWindow
from Dialogs.DLog_Alert import DLG_Alert
from Dialogs.DLog_Oneline_Input import DLG_Oneline_Input

class Payment_Window(QMainWindow, Ui_MainWindow):
    
    cancel_btnsgl = QtCore.pyqtSignal()
    atrans_btnsgl = QtCore.pyqtSignal()
    db = dbcont()
    
    def __init__(self,SProdList = None):
        super(Payment_Window,self).__init__()
        self.prodlist = None
        self.setupUi(self)
        
        if SProdList == None:
            self.prodlist = []
        else:
            self.prodlist = SProdList
            
        self.onlyInt = QIntValidator()
        self.Discount_LE.setValidator(self.onlyInt)
        
        self.Home_btn.clicked.connect(lambda: print(self.prodlist))

        self.Cash_btn.clicked.connect(self.confirmed_payment_cash)
        self.GCash_btn.clicked.connect(self.confirmed_payment_Gcash)
        self.Cancel_btn.clicked.connect(self.prev_window)
        self.Cancel_btn.clicked.connect(self.prev_window)
        self.Discount_LE.textChanged.connect(self.set_totalprice)
        
    def clean_screen(self):
        self.Product_Table.setRowCount(0)
        self.TPrice_L.setText('0')
        self.Discount_LE.clear()
        
    def prev_window(self):
        self.clean_screen()
        self.cancel_btnsgl.emit()

    def init_screen(self):
        self.set_totalprice()
        self.set_table_elements()
        print(self.prodlist)
    
    def set_totalprice(self):
        totalprice = 0
        for prod in self.prodlist:
            totalprice += self.db.prod_price(id= prod[0]) * float(prod[2])
        
        self.SPrice_L.setText(str(totalprice))
        if self.Discount_LE.text() != '' :
            dc = float(self.Discount_LE.text())
            if 0 <= dc and dc <= 100:
                totalprice -= (float(totalprice) * (float(self.Discount_LE.text())/100))
                self.TPrice_L.setText(str(totalprice))
            else:
                Dlg = DLG_Alert(msg= 'Ranging from 0 - 100 Only!')
                Dlg.exec()
        else:
            self.TPrice_L.setText(str(totalprice))
        
    def confirmed_payment_cash(self):
        if int(self.Paid_LE.text()) < int(self.TPrice_L.text()):
            Dlg = DLG_Alert(msg='Insufficient money entered!')
            Dlg.exec()
        else:
                print(self.prodlist)
                self.db.add_sold_receipt(Price= self.TPrice_L.text(), PPrice= self.Paid_LE.text(),
                                        SoldProductsList= self.prodlist, GCashRef=None)
                Dlg = DLG_Alert()
                Dlg.exec()
        
    def confirmed_payment_Gcash(self):
        if int(self.Paid_LE.text()) < int(self.TPrice_L.text()):
            Dlg = DLG_Alert(msg='Insufficient money entered!')
            Dlg.exec()
        else:
            Dlg_GCash = DLG_Oneline_Input(msg='GCash Reference:')
            Dlg_GCash.Input_LE.setValidator(self.onlyInt)
            Dlg_GCash.Input_LE.setMaxLength(13)
            print(self.prodlist)
            Dlg_GCash.exec()
            self.db.add_sold_receipt(Price= self.TPrice_L.text(), PPrice= self.Paid_LE.text(),
                                    SoldProductsList= self.prodlist, GCashRef=Dlg_GCash.Input_LE.Text())
            Dlg = DLG_Alert()
            Dlg.exec()
        
    def set_table_elements(self):
        self.Product_Table.setRowCount(len(self.prodlist))
        for row_number, row_data in enumerate(self.prodlist):
            for column_number, data in enumerate(row_data):
                self.Product_Table.setItem(row_number, column_number, QTableWidgetItem(str(data)))