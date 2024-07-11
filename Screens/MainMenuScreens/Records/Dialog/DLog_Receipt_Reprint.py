from PyQt5.QtWidgets import  QWidget, QVBoxLayout, QLabel, QDialog,QHBoxLayout ,QSpacerItem, QSizePolicy
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtGui import QPainter, QTransform
from PyQt5.QtCore import QSizeF

from Database.User_Manager import UserMana
from Database.DBController import dbcont

from .DLog_Receipt_Reprint_2_ui import Ui_Dialog

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
        self.Print_btn.clicked.connect(self.handlePrint)
        
    def create_prodlist(self):
        
        prodlistlayout = QVBoxLayout()
        
        for prod in self.Plist:
            dbprod = self.db.get_prod_search(searchstr= prod[0], searchcate= -1)
            labelwidget = QWidget()
            layout = QHBoxLayout()
            spacer1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
            spacer2 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
            spacer3 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
            
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
        
    def handlePrint(self):
        printer = QPrinter()

        print_dialog = QPrintDialog(printer, self)
        if print_dialog.exec_() == QPrintDialog.Accepted:
            self.printContent(printer)
        
    def printContent(self, printer):
        
        # widget_size = self.widget.size()
        # widget_width = widget_size.width()
        # widget_height = widget_size.height()

        # # Set paper size
        # resolution = printer.resolution()
        # paper_size = QSizeF(widget_width / resolution * 25.4, widget_height / resolution * 25.4)  # Convert pixels to mm

        # printer.setPaperSize(paper_size, QPrinter.Millimeter)
        # printer.setFullPage(True)

        # # Set margins
        # printer.setPageMargins(0, 0, 0, 0, QPrinter.Millimeter)
        
        # painter = QPainter(printer)
        # self.widget.render(painter)
        # painter.end()
                
        widget_size = self.widget.size()
        widget_width = widget_size.width()
        widget_height = widget_size.height()

        # Set paper size
        resolution = printer.resolution()
        # Set paper width to 80mm
        paper_width_mm = 58  # 80mm wide paper
        paper_width_pixels = paper_width_mm / 25.4 * resolution  # Convert mm to pixels

        # Calculate the scaling factor
        scale_factor = paper_width_pixels / widget_width

        # Adjust paper height based on scale factor
        scaled_widget_height = widget_height * scale_factor
        paper_height_mm = scaled_widget_height / resolution * 25.4  # Convert pixels to mm

        paper_size = QSizeF(paper_width_mm, paper_height_mm)
        printer.setPaperSize(paper_size, QPrinter.Millimeter)
        printer.setFullPage(True)

        # Set margins
        printer.setPageMargins(0, 0, 0, 0, QPrinter.Millimeter)

        # Print
        painter = QPainter(printer)
        transform = QTransform()
        transform.scale(scale_factor, scale_factor)
        painter.setTransform(transform)
        self.widget.render(painter)
        painter.end()