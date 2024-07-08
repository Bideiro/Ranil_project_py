from PyQt5.QtWidgets import QDialog, QWidget, QVBoxLayout,QHBoxLayout ,QSpacerItem, QSizePolicy, QLabel
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QSizeF

from Database.User_Manager import UserMana
from Database.DBController import dbcont

from .DLog_Receipt_ui import Ui_Dialog

class DLG_Receipt(QDialog, Ui_Dialog):
    
    db = dbcont()
    User = UserMana()
    
    def __init__(self, prodlist, Tprice ,Ptype ,Pprice, RID, DTime, GCRef, parent = None):
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
            spacer2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
            spacer3 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
            
            qty = QLabel(str(prod[2]))
            price = QLabel(str(dbprod[0][2]))
            prodname = QLabel(str(dbprod[0][1]))
            inttprice = int(prod[2]) * int(dbprod[0][2])
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
        # # Get the size of the widget
        # widget_size = self.label.size()
        
        # # Convert widget size to points (1 inch = 72 points)
        # dpi = printer.resolution()
        # width_points = widget_size.width() * 72 / self.logicalDpiX()
        # height_points = widget_size.height() * 72 / self.logicalDpiY()
        # printer.setPaperSize(QSizeF(width_points, height_points), QPrinter.Point)
        # printer.setFullPage(True)
        
        # # Set margins to zero
        # printer.setPageMargins(0, 0, 0, 0, QPrinter.Point)
        
        # # Create a QPainter and set it to the printer
        # painter = QPainter(printer)
        
        # # Scale the painter to match the printer resolution
        # scale_x = dpi / self.logicalDpiX()
        # scale_y = dpi / self.logicalDpiY()
        # painter.scale(scale_x, scale_y)
        
        # # Render the specific widget (self.label in this case)
        # self.widget.render(painter)
        
        # # End the painter to finalize the printing
        
        widget_size = self.widget.size()
        widget_width = widget_size.width()
        widget_height = widget_size.height()

        # Set paper size
        resolution = printer.resolution()
        paper_size = QSizeF(widget_width / resolution * 25.4, widget_height / resolution * 25.4)  # Convert pixels to mm

        printer.setPaperSize(paper_size, QPrinter.Millimeter)
        printer.setFullPage(True)

        # Set margins
        printer.setPageMargins(0, 0, 0, 0, QPrinter.Millimeter)
        
        painter = QPainter(printer)
        self.widget.render(painter)
        painter.end()
