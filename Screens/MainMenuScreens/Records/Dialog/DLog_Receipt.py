from PyQt5.QtWidgets import QDialog, QWidget, QVBoxLayout,QHBoxLayout ,QSpacerItem, QSizePolicy, QLabel

from Database.User_Manager import UserMana
from Database.DBController import dbcont

from .DLog_Receipt_ui import Ui_Dialog

class DLG_Receipt_Reprint(QDialog, Ui_Dialog):
    
    db = dbcont()
    User = UserMana()
    
    def __init__(self, prodlist, Tprice ,Ptype, Pprice, RID, DTime, GCRef, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.Plist = prodlist
        
        self.setWindowTitle(f'Showing Receipt No: {RID}')
        
        self.create_prodlist()
        
        usercreds = self.db.get_user_creds(RUID= self.User.RUID)
        
        if usercreds[8] != 0:
            suffix = self.db.get_suffix(id= usercreds[8])
        else:
            suffix = ''
        if usercreds[7] == None or usercreds[7] == '':
            whole_name = str(usercreds[5]) + ' ' + str(usercreds[6]) + ' ' + str(suffix)
        else:
            whole_name = str(usercreds[5]) + ' ' + str(usercreds[7]) + ' ' + str(usercreds[6]) + ' ' + str(suffix)
            
        
        self.UName_L.setText(whole_name)
        self.APaid_L.setText(str(Pprice))
        self.ReceiptNo_L.setText(str(RID))
        self.DateTime_L.setText(str(DTime))
        self.INumber_L.setText(str(len(self.Plist)))
        self.TotalPrice_L.setText(str(Tprice))
        if Ptype == 0:
            self.PMethod_L.setText('Payment Type: Cash')
        elif Ptype == 1:
            self.PMethod_L.setText('Payment Type: GCash')
        else:
            self.PMethod_L.setText('Payment Type: Split Payment ( GCash + Cash )')
        
        if GCRef == '' or GCRef == None:
            GCRef = "None"
            
        self.GCRef_L.setText(str(GCRef))
        
    def create_prodlist(self):
        
        prodlistlayout = QVBoxLayout()
        
        for prod in self.Plist:
            dbprod = self.db.get_prod_search(searchstr= prod[0], searchcate= -1)
            labelwidget = QWidget()
            layout = QHBoxLayout()
            spacer1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
            spacer2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
            spacer3 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
            
            qty = QLabel(str(prod[2]))
            price = QLabel(str(prod[1]))
            prodname = QLabel(str(dbprod[0][1]))
            inttprice = int(prod[1]) * int(prod[2])
            tprice = QLabel(str(inttprice))
            
            layout.addWidget(prodname)
            layout.addItem(spacer1)
            layout.addWidget(price)
            layout.addItem(spacer2)
            layout.addWidget(qty)
            layout.addItem(spacer3)
            layout.addWidget(tprice)
            
            labelwidget.setLayout(layout)
            prodlistlayout.addWidget(labelwidget)
        
        self.ProdList_w.setLayout(prodlistlayout)