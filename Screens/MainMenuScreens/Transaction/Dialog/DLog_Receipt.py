import sys
from PyQt5.QtWidgets import QDialog, QPushButton, QWidget, QVBoxLayout,QHBoxLayout ,QSpacerItem, QSizePolicy, QLabel
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtGui import QPainter

from PyQt5.QtCore import Qt

from Database.DBController import dbcont

from .DLog_Receipt_ui import Ui_Dialog
from Dialogs.DLog_Alert import DLG_Alert

class DLG_Receipt(QDialog, Ui_Dialog):
    
    db = dbcont()
    
    def __init__(self, prodlist, Tprice ,Ptype, Pprice, RID, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.Popup)
        self.Plist = prodlist
        self.create_prodlist()
        self.TotalPrice_L.setText(str(Tprice))
        if Ptype == 0:
            self.PMethod_L.setText('Cash')
        elif Ptype == 1:
            self.PMethod_L.setText('GCash')
        else:
            self.PMethod_L.setText('Split Payment ( GCash + Cash )')
        self.APaid_L.setText(str(Pprice))
        self.RID_L.setText(str(RID))
        
    def create_prodlist(self):
        
        prodlistlayout = QVBoxLayout()
        
        for prod in self.Plist:
            dbprod = self.db.get_prod_search(searchstr= prod[0], searchcate= -1)
            labelwidget = QWidget()
            layout = QHBoxLayout()
            spacer1 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
            spacer2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
            spacer3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
            
            qty = QLabel(prod[2])
            price = QLabel(str(dbprod[0][2]))
            prodname = QLabel(prod[1])
            inttprice = int(prod[2]) * int(dbprod[0][2])
            tprice = QLabel(str(inttprice))
            
            layout.addWidget(qty)
            layout.addItem(spacer1)
            layout.addWidget(price)
            layout.addItem(spacer2)
            layout.addWidget(prodname)
            layout.addItem(spacer3)
            layout.addWidget(tprice)
            
            labelwidget.setLayout(layout)
            prodlistlayout.addWidget(labelwidget)
        
        self.ProdList_w.setLayout(prodlistlayout)