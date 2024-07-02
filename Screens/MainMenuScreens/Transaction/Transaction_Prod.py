import os
from PyQt5.QtWidgets import QMainWindow,QVBoxLayout,QHBoxLayout , QTableWidgetItem, QWidget, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QIntValidator
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QPushButton
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QSizeF, QStandardPaths, QDateTime


from Database.DBController import dbcont
from .Transaction_Prod_ui import Ui_MainWindow

from Dialogs.DLog_Alert import DLG_Alert
from .Dialog.DLog_CashAmount import DLG_CashAmount
from .Dialog.DLog_GCash import DLG_GCash
from .Dialog.DLog_PaymentCombined import DLG_SplitPayment
from .Dialog.DLog_Receipt import DLG_Receipt

from Dialogs.DLog_Confirm import DLG_Confirm
from PyQt5 import QtCore

class Trans_Prod_Window(QMainWindow, Ui_MainWindow):
    resize_sgl = QtCore.pyqtSignal()
    
    db = dbcont()
    
    Sprod = None
    StableRPID = set()
    SProdConfirmed = []
    SprodRow = None
    TotalPrice = None
    
    amtpaid = None
    GCashRef = None
    
    def __init__(self, parent= None):
        super(Trans_Prod_Window,self).__init__(parent)
        self.setupUi(self)
        # self.reset_page()
        
        self.onlyInt = QIntValidator()
        self.Quantity_LE.setValidator(self.onlyInt)
        self.Discount_LE.setValidator(self.onlyInt)
        
        # Main widget
        self.Cate_CB.addItem('All')
        self.Cate_CB.addItems(self.db.get_cate(all=True))
        self.Cate_CB.currentIndexChanged.connect(self.sort_search_table)
        
        self.Search_btn.clicked.connect(self.sort_search_table)
        self.CSearch_btn.clicked.connect(self.set_tableElements)
        
        self.Product_Table.itemClicked.connect(self.add_to_list)
        
        # Order Widget
        self.RProduct_btn.clicked.connect(self.remove_sprod)
        self.Quantity_LE.textChanged.connect(self.add_quantity)
        
        self.Done_btn.clicked.connect(self.change_widget)
        self.Clear_btn.clicked.connect(self.clean_sprod_table)
        
        self.SProducts_Table.itemClicked.connect(self.clicked_item_sprod)
        
        # Final Widget
        self.PReceipt_btn.setEnabled(False)
        self.Discount_LE.textChanged.connect(self.set_totalprice)
        self.FCancel_btn.clicked.connect(self.change_widget)
        self.FCash_btn.clicked.connect(self.confirmed_payment_cash)
        self.FGcash_btn.clicked.connect(self.confirmed_payment_GCash)
        self.ATrans_btn.clicked.connect(self.another_trans)
        self.SPayment_btn.clicked.connect(self.confirmed_split_payment)
        self.PReceipt_btn.clicked.connect(self.print_widget)
                
    def search(self):
        self.Product_Table.setRowCount(0)
        searchResult = self.db.search_prod( searchstr= self.Search_LE.text(), trans= True)
        if searchResult:
            self.Product_Table.setRowCount(len(searchResult))
            for row_number, row_data in enumerate(searchResult):
                self.Product_Table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if column_number == 6:
                        data = self.db.get_id_value(id= data, unit= True)
                    if column_number == 7:
                        data = self.db.get_id_value(id= data, cate= True)
                    self.Product_Table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
    def clicked_item_sprod(self, item):
        Sprod = self.db.search_prod(searchstr= self.SProducts_Table.item(item.row(), 0).text() ,id=True)
        self.SprodRow = item.row()
        self.PName_L.setText(Sprod[1])
        self.RUID_L.setText(Sprod[0])
        self.SPrice_L.setText(str(Sprod[2]))
        self.EDate_L.setText(str(Sprod[4]))
        self.Quantity_LE.setText(self.SProducts_Table.item(item.row(), 2).text())
        
    def remove_sprod(self):
        if self.SprodRow != None:
            RPID_item = self.SProducts_Table.item(self.SprodRow, 0)
            self.StableRPID.discard(RPID_item.text())
            
            for item in self.SProdConfirmed[:]:
                if item[0] == RPID_item:
                    self.SProdConfirmed.remove(item)
            
            self.SProducts_Table.removeRow(self.SprodRow)
            self.SprodRow = None
            self.current_prod_reset()
        else:
            Dlg = DLG_Alert(msg='No Selected Product in order list!')
            Dlg.exec()
        
    def add_to_list(self,item):
        row = item.row()
        column_count = self.Product_Table.columnCount()
        prod_values = []
        
        for column in range(column_count):
            cell_item = self.Product_Table.item(row, column)
            if cell_item is not None:
                prod_values.append(cell_item.text())
            
        self.PName_L.setText(prod_values[1])
        self.RUID_L.setText(prod_values[0])
        self.SPrice_L.setText(prod_values[2])
        self.EDate_L.setText(prod_values[4])
        
        self.Sprod = [prod_values[0],prod_values[1],prod_values[2],prod_values[3],prod_values[4],'1']
        
        if self.Sprod:
            if self.Sprod[3] == '0':
                Dlg = DLG_Alert(msg=f'{self.Sprod[1]}({self.Sprod[0]}) has 0 Stock!')
                Dlg.exec()
                
            elif self.Sprod[0] not in self.StableRPID:
                self.StableRPID.add(self.Sprod[0])
                rowpos = self.SProducts_Table.rowCount()
                self.SProducts_Table.insertRow(rowpos)
                
                for col, data in enumerate(self.Sprod):
                    if col == 2:
                        self.SProducts_Table.setItem(rowpos, col, QTableWidgetItem(str(self.Sprod[5])))
                    elif col == 0 or col == 1:
                        self.SProducts_Table.setItem(rowpos, col, QTableWidgetItem(str(data)))
            else:
                Dlg = DLG_Alert(msg='Already in list!')
                Dlg.exec()
        else:
            Dlg = DLG_Alert(msg='No Selected Item!')
            Dlg.exec()
        
    def add_quantity(self):
        selquantity = None
        for row in range(self.SProducts_Table.rowCount()):
            item = self.SProducts_Table.item(row, 0)
            if item.text() == self.Sprod[0]:
                selquantity = self.SProducts_Table.item(row, 2)
                break
        
        if selquantity is not None:
            
            if self.Quantity_LE.text() == '':
                pass
            elif self.Quantity_LE.text() == '0' or int(self.Quantity_LE.text()) <= 0:
                Dlg = DLG_Alert(msg='Quantity cant be 0 or less than 0!')
                Dlg.exec()
            elif int(self.Quantity_LE.text()) <= int(self.Sprod[3])  :
                row = selquantity.row()
                self.SProducts_Table.setItem(row,2,QTableWidgetItem(self.Quantity_LE.text()))
            else:
                Dlg = DLG_Alert(msg='Not enough stock!')
                Dlg.exec()
        else:
            Dlg = DLG_Alert(msg='Selected item was removed or not Added!')
            Dlg.exec()

    def confirmed_order(self):
        self.SProdConfirmed = []
        for row in range(self.SProducts_Table.rowCount()):
            row_data = []
            for col in range(self.SProducts_Table.columnCount()):
                item = self.SProducts_Table.item(row, col)
                row_data.append(item.text())
            self.SProdConfirmed.append(row_data)
            
        hasamount = True
        for data in self.SProdConfirmed:
            if int(data[2]) == 0:
                Dlg = DLG_Alert(msg= f'Item: {data[1]} has no amount!')
                Dlg.exec()
                hasamount = False
                
        if hasamount:
            if self.SProdConfirmed == []:
                Dlg = DLG_Alert(msg='No selected products!')
                Dlg.exec()
            else:
                self.set_final_table_elements()
                self.set_totalprice()
                self.Order_w.setVisible(False)
                self.FReceipt_w.setVisible(True)
    
    # all about final

    def confirmed_payment_cash(self):
        Dlg = DLG_CashAmount(price=self.TotalPrice)
        Dlg.exec()
        if Dlg.result() == 1:
            self.amtpaid = Dlg.Input_LE.text()
            self.init_payment_protocol(payment= 0)
        
    def confirmed_payment_GCash(self):
        Dlg = DLG_GCash(price=self.TotalPrice)
        Dlg.exec()
        if Dlg.result() == 1:
            self.amtpaid = Dlg.Input_LE.text()
            self.GCashRef = Dlg.Input2_LE.text()
            self.init_payment_protocol(payment= 1)

    def confirmed_split_payment(self):
        Dlg = DLG_SplitPayment(price=self.TotalPrice)
        Dlg.exec()
        if Dlg.result() == 1:
            self.amtpaid = int(Dlg.Input_LE.text()) + int(Dlg.Input3_LE.text())
            self.GCashRef = Dlg.Input2_LE.text()
            self.init_payment_protocol(payment= 2)
    
    def init_payment_protocol(self, payment):
        self.db.add_sold_protocol(
            Price= self.TPrice_L.text(), PPrice= self.amtpaid,
            SoldProductsList= self.SProdConfirmed,
            GCashRef= self.GCashRef, Ptype= payment
        )
        self.dlg_receipt = DLG_Receipt(prodlist=self.SProdConfirmed,Tprice= self.TotalPrice,
                                    Ptype= payment, Pprice= self.amtpaid, RID = self.db.get_recent_receiptID())
        self.dlg_receipt.exec()
        self.PReceipt_btn.setEnabled(True)
    
    def set_totalprice(self):
        totalprice = 0
        for prod in self.SProdConfirmed:
            totalprice += self.db.prod_price(id= prod[0]) * float(prod[2])
        self.TotalPrice = totalprice
        self.STotal_L.setText(str(totalprice))
        if self.Discount_LE.text() != '' :
            dc = float(self.Discount_LE.text())
            if 0 <= dc and dc <= 100:
                totalprice -= (float(totalprice) * (float(self.Discount_LE.text())/100))
                self.TPrice_L.setText(str(totalprice))
                self.TotalPrice = totalprice
            else:
                Dlg = DLG_Alert(msg= 'Ranging from 0 - 100 Only!')
                Dlg.exec()
        else:
            self.TPrice_L.setText(str(totalprice))
    
    def set_final_table_elements(self):
        self.FProduct_Table.setRowCount(len(self.SProdConfirmed))
        for row_number, row_data in enumerate(self.SProdConfirmed):
            for column_number, data in enumerate(row_data):
                self.FProduct_Table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    
    def print_widget(self):
        printer = QPrinter()
        output_directory = QStandardPaths.writableLocation(QStandardPaths.DesktopLocation)
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        
        # Get current date and time
        current_datetime = QDateTime.currentDateTime()
        timestamp = current_datetime.toString('yyyyMMdd_hh_mm')

        output_file = os.path.join(output_directory, f'Receipt_{self.dlg_receipt.RID_L.text()}_{timestamp}.pdf')
        printer.setOutputFileName(output_file)
        
        # Adjust widget size
        widget_size = self.dlg_receipt.size()
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
        self.dlg_receipt.render(painter)
        painter.end()
        print(f'Saved PDF to {output_file}')
    
    
    # all about screens
    def clean_sprod_table(self):
        self.SProdConfirmed =[]
        self.StableRPID.clear()
        self.SProducts_Table.setRowCount(0)
        
    def current_prod_reset(self):
        self.PName_L.setText(None)
        self.RUID_L.setText(None)
        self.SPrice_L.setText(None)
        self.EDate_L.setText(None)
        self.Quantity_LE.setText(None)
        
    def another_trans(self):
        Dlg = DLG_Confirm()
        Dlg.exec()
        
        if Dlg.result() == 1:
            self.change_widget()
            self.reset_page()
        
    def change_widget(self):
        if self.FReceipt_w.isVisible():
            self.Order_w.setVisible(True)
            self.FReceipt_w.setVisible(False)
            self.resize_sgl.emit()
        else:
            self.resize_sgl.emit()
            self.confirmed_order()
            print(self.SProdConfirmed)
    
    def reset_page(self):
        self.FReceipt_w.setVisible(False)
        self.Main_w.setVisible(False)
        self.Order_w.setVisible(False)
        self.BList_w.setVisible(True)
        self.set_dybutton()
        self.set_tableElements()
        self.clean_sprod_table()
        
    def set_dybutton(self):
        layout = QHBoxLayout()
        widget = QWidget()
        mainlayout = QVBoxLayout()
        cate_list = self.db.get_cate(all=True)
        cate_list.insert(0, 'All')
        cnt = 0
        for index, label in enumerate(cate_list):
            cnt += 1
            button = QPushButton(label, self)
            button.clicked.connect(self.on_button_click)
            # Setting button design
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
            button.setSizePolicy(sizePolicy)
            button.setMinimumSize(QtCore.QSize(50, 50))
            button.setProperty('buttonNumber', index)
            # --END--
            layout.addWidget(button)
            
            if cnt % 3 == 0:
                widget.setLayout(layout)
                mainlayout.addWidget(widget)
                layout = QHBoxLayout()
                widget = QWidget()
            elif cnt == len(cate_list):
                widget.setLayout(layout)
                mainlayout.addWidget(widget)
                layout = QHBoxLayout()
                widget = QWidget()
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Expanding)
        mainlayout.addItem(spacer)
        self.Buttons_w.setLayout(mainlayout)

    # def set_dybutton(self):
    #     # Function to clear existing layout
    #     def clear_layout(layout):
    #         if layout is not None:
    #             while layout.count():
    #                 item = layout.takeAt(0)
    #                 widget = item.widget()
    #                 if widget is not None:
    #                     widget.deleteLater()
    #                 else:
    #                     sub_layout = item.layout()
    #                     if sub_layout is not None:
    #                         clear_layout(sub_layout)
    #             layout.deleteLater()

    #     # Clear the existing layout of Buttons_w
    #     old_layout = self.Buttons_w.layout()
    #     if old_layout is not None:
    #         clear_layout(old_layout)

    #     # Create new main layout
    #     mainlayout = QVBoxLayout()

    #     # Get the updated category list
    #     cate_list = self.db.get_cate(all=True)
    #     cate_list.insert(0, 'All')

    #     # Initialize layout variables
    #     layout = QHBoxLayout()
    #     widget = QWidget()
    #     cnt = 0

    #     for index, label in enumerate(cate_list):
    #         cnt += 1
    #         button = QPushButton(label, self)
    #         button.clicked.connect(self.on_button_click)

    #         # Setting button design
    #         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
    #         sizePolicy.setHorizontalStretch(0)
    #         sizePolicy.setVerticalStretch(0)
    #         sizePolicy.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
    #         button.setSizePolicy(sizePolicy)
    #         button.setMinimumSize(QtCore.QSize(50, 50))
    #         button.setProperty('buttonNumber', index)
    #         # --END--
    #         layout.addWidget(button)

    #         if cnt % 3 == 0 or cnt == len(cate_list):
    #             widget.setLayout(layout)
    #             mainlayout.addWidget(widget)
    #             layout = QHBoxLayout()
    #             widget = QWidget()

    #     # Add spacer at the end of the layout
    #     spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Expanding)
    #     mainlayout.addItem(spacer)

    #     # Set the new layout
    #     self.Buttons_w.setLayout(mainlayout)
    #     self.Buttons_w.update()  # Ensure the widget updates with the new layout

    #     # Debugging: Print statements to ensure layout is set
    #     print("New layout set with {} categories.".format(len(cate_list)))
    #     print("Main layout item count:", mainlayout.count())

    def on_button_click(self):
        sender = self.sender()
        self.Main_w.setVisible(True)
        self.Order_w.setVisible(True)
        self.BList_w.setVisible(False)
        self.resize_sgl.emit()
        self.Cate_CB.setCurrentIndex(sender.property('buttonNumber'))
        
    def sort_search_table(self):
        cbcurr = self.Cate_CB.currentIndex()
        cbcurr -= 1
            
        searchstr = self.Search_LE.text()
        if searchstr == '':
            if cbcurr == -1:
                searchResult = self.db.get_prod_search(all=True)
            else:
                searchResult = self.db.get_prod_search(searchcate= cbcurr)
        else:
            searchResult = self.db.get_prod_search(searchstr= searchstr, searchcate= cbcurr)
        self.Product_Table.setRowCount(0)
        if searchResult:
            self.Product_Table.setRowCount(len(searchResult))
            for row_number, row_data in enumerate(searchResult):
                self.Product_Table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if column_number == 6:
                        data = self.db.get_id_value(id= data, unit= True)
                    if column_number == 7:
                        data = self.db.get_id_value(id= data, cate= True)
                    self.Product_Table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
    def set_tableElements(self):
        result = self.db.get_all_prod(trans= True)
        self.Search_LE.clear()
        self.Cate_CB.setCurrentIndex(0)
        self.Product_Table.setRowCount(len(result))
        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):
                self.Product_Table.setItem(row_number, column_number, QTableWidgetItem(str(data)))