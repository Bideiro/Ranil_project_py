import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .MainMenu_ui import Ui_MainWindow

from .MainMenuScreens.Home import HomeWindow

from .MainMenuScreens.Security.User_Information import User_Information_Window

from .MainMenuScreens.Registration.Registration_1 import Registration_1_Window
from .MainMenuScreens.Registration.Registration_prod import Registration_prod_Window
from .MainMenuScreens.Registration.Registration_user import Registration_user_Window

from .MainMenuScreens.Sales.Sales import Sales_Window

from .MainMenuScreens.Transaction.Transaction_Prod import Trans_Prod_Window

from .MainMenuScreens.Inventory.Inventory import Inventory_Window

from .MainMenuScreens.Records.Records_1 import Records_1_Window
from .MainMenuScreens.Records.Supplier_Record import Supp_Rec_Window
from .MainMenuScreens.Records.Add_Receipt import add_reciept_Window
from .MainMenuScreens.Records.Transaction_Records import Trans_Rec_Window

from .MainMenuScreens.Reports.Reports_1 import Reports_1_Window
from .MainMenuScreens.Reports.Sales_Report import Sales_Report_Window
from .MainMenuScreens.Reports.Inventory_Report import Inventory_Report_Window
from .MainMenuScreens.Reports.User_Logs import User_Logs_Window

from .MainMenuScreens.Help.Help_1 import HelpWindow
from .MainMenuScreens.Maintenance.Maintenance_1 import Maintenance_Window
from .MainMenuScreens.About.About import AboutWindow

from Database.DBController import dbcont
from Database.User_Manager import UserMana
from PyQt5 import QtWidgets, QtGui, QtCore
class MainMenuWindow( QMainWindow, Ui_MainWindow):
    
    log_out_btnsgl = QtCore.pyqtSignal()
    resize_trig = QtCore.pyqtSignal()
    User = UserMana()
    db = dbcont()
    
    def __init__(self):
        super(MainMenuWindow,self).__init__()
        self.setupUi(self)
        
        # Initializing Screens
        
        self.Home = HomeWindow()
        self.stackedWidget.addWidget(self.Home)
        self.stackedWidget.setCurrentWidget(self.Home)
        self.CScreen_L.setText('> Home')
        
        self.User_Info = User_Information_Window()
        self.stackedWidget.addWidget(self.User_Info)
        
        self.Reg_1 = Registration_1_Window()
        self.Reg_prod = Registration_prod_Window()
        self.Reg_user = Registration_user_Window()
        self.stackedWidget.addWidget(self.Reg_1)
        self.stackedWidget.addWidget(self.Reg_prod)
        self.stackedWidget.addWidget(self.Reg_user)
        
        self.Sales = Sales_Window()
        self.stackedWidget.addWidget(self.Sales)
        self.Trans_prod = Trans_Prod_Window()
        self.stackedWidget.addWidget(self.Trans_prod)
        self.Inven = Inventory_Window()
        self.stackedWidget.addWidget(self.Inven)
        
        self.Records_1 = Records_1_Window()
        self.Supp_Receipts = Supp_Rec_Window()
        self.Add_Supp_Receipt = add_reciept_Window()
        self.stackedWidget.addWidget(self.Records_1)
        self.stackedWidget.addWidget(self.Supp_Receipts)
        self.stackedWidget.addWidget(self.Add_Supp_Receipt)
        
        
        self.Reports_1 = Reports_1_Window()
        self.Inventory_Report = Inventory_Report_Window()
        self.Trans_Receipts = Trans_Rec_Window()
        self.User_Logs = User_Logs_Window()
        self.stackedWidget.addWidget(self.Trans_Receipts)
        self.stackedWidget.addWidget(self.Reports_1)
        self.stackedWidget.addWidget(self.Inventory_Report)
        self.stackedWidget.addWidget(self.User_Logs)
        
        self.Sales_Report = Sales_Report_Window()
        self.stackedWidget.addWidget(self.Sales_Report)
        
        self.Help = HelpWindow()
        self.Main_1 = Maintenance_Window()
        self.about = AboutWindow()
        self.stackedWidget.addWidget(self.Help)
        self.stackedWidget.addWidget(self.Main_1)
        self.stackedWidget.addWidget(self.about)
        
        # Initializationg of Menu
        
        # Sidebar visibility
        self.scrollArea.setVisible(False)
        self.menu_btn.toggled['bool'].connect(self.scrollArea.setVisible)
        
        # Signal Recievers
        
        # For resizing the window
        self.Trans_prod.resize_sgl.connect(self.window_size_handler)
        
        # Registration Buttons
        self.Reg_1.prod_reg_btnsgl.connect(lambda: self.stackedWidget.setCurrentWidget(self.Reg_prod))
        self.Reg_1.user_reg_btnsgl.connect(lambda: self.stackedWidget.setCurrentWidget(self.Reg_user))
        
        self.Reg_prod.back_btnsgl.connect(lambda: self.stackedWidget.setCurrentWidget(self.Reg_1))
        self.Reg_user.back_btnsgl.connect(lambda: self.stackedWidget.setCurrentWidget(self.Reg_1))
        
        # Records Buttons
        self.Records_1.SReciepts_btnsgl.connect(lambda: self.stackedWidget.setCurrentWidget(self.Supp_Receipts))
        self.Records_1.TReceipts_btnsgl.connect(lambda: self.stackedWidget.setCurrentWidget(self.Trans_Receipts))
        
        self.Supp_Receipts.back_btnsgl.connect(lambda: self.stackedWidget.setCurrentWidget(self.Records_1))
        self.Supp_Receipts.Add_btnsgl.connect(self.toaddsuppreceipt)
        self.Add_Supp_Receipt.Finish_btnsgl.connect(self.addsuppfinish_btn)
        self.Add_Supp_Receipt.Back_btnsgl.connect(lambda: self.stackedWidget.setCurrentWidget(self.Supp_Receipts))
        self.Trans_Receipts.back_btnsgl.connect(lambda: self.stackedWidget.setCurrentWidget(self.Records_1))
        # Reports Buttons
        
        self.Reports_1.Inven_btnsgl.connect(lambda: self.stackedWidget.setCurrentWidget(self.Inventory_Report))
        self.Reports_1.Sales_btnsgl.connect(lambda: self.stackedWidget.setCurrentWidget(self.Sales_Report))
        self.Reports_1.ULogs_btnsgl.connect(lambda: self.stackedWidget.setCurrentWidget(self.User_Logs))
        #Log Out
        self.log_out_sdbtn.clicked.connect(self.init_log_out)
        
    def toaddsuppreceipt(self):
        self.Add_Supp_Receipt.RNumber_LE.clear()
        self.stackedWidget.setCurrentWidget(self.Add_Supp_Receipt)
        
    def addsuppfinish_btn(self):
        self.Supp_Receipts.set_tableElements()
        self.stackedWidget.setCurrentWidget(self.Supp_Receipts)
        
    def refresh_logs(self):
        self.User_Logs.set_tableElements()
        self.stackedWidget.setCurrentWidget(self.User_Logs)
        
    def init_log_out(self):
        self.security_sdbtn.setChecked(False)
        self.registration_sdbtn.setChecked(False)
        self.sales_sdbtn.setChecked(False)
        self.transaction_sdbtn.setChecked(False)
        self.inventory_sdbtn.setChecked(False)
        self.records_sdbtn.setChecked(False)
        self.reports_sdbtn.setChecked(False)
        self.maintenance_sdbtn.setChecked(False)
        self.about_sdbtn.setChecked(False)
        self.help_sdbtn.setChecked(False)
        self.stackedWidget.setCurrentWidget(self.Home)
        self.db.log_action(action='Logged Out')
        self.log_out_btnsgl.emit()
        
    def window_size_handler(self):
        print('resizing')
        currentWidget = self.stackedWidget.currentWidget()
        self.resize(currentWidget.minimumSizeHint())
        self.resize_trig.emit()
    
    @pyqtSlot()
    # Functions changing windows
    
    def on_home_tpbtn_clicked(self):
        self.stackedWidget.setCurrentWidget(self.Home)
    
    def on_security_sdbtn_clicked(self):
        self.CScreen_L.setText('> Security')
        self.User_Info.createlist()
        self.stackedWidget.setCurrentWidget(self.User_Info)
        
    def on_registration_sdbtn_clicked(self):
        self.CScreen_L.setText('> Registration')
        self.Reg_prod.PName_LE.clear()
        self.Reg_prod.SPrice_LE.clear()
        self.Reg_prod.Desc_PTE.clear()
        self.stackedWidget.setCurrentWidget(self.Reg_1)
        
    def on_sales_sdbtn_clicked(self):
        self.CScreen_L.setText('> Sales')
        self.Sales.set_tableElements()
        self.stackedWidget.setCurrentWidget(self.Sales)
        
    def on_transaction_sdbtn_clicked(self):
        self.CScreen_L.setText('> Transaction')
        self.Trans_prod.reset_page()
        self.stackedWidget.setCurrentWidget(self.Trans_prod)
        
    def on_inventory_sdbtn_clicked(self):
        self.CScreen_L.setText('> Inventory')
        self.Inven.set_tableElements()
        self.stackedWidget.setCurrentWidget(self.Inven)
        
    def on_records_sdbtn_clicked(self):
        self.CScreen_L.setText('> Records')
        self.stackedWidget.setCurrentWidget(self.Records_1)
        
    def on_reports_sdbtn_clicked(self):
        self.CScreen_L.setText('> Reports')
        self.stackedWidget.setCurrentWidget(self.Reports_1)
        
    def on_help_sdbtn_clicked(self):
        self.CScreen_L.setText('> Help')
        self.stackedWidget.setCurrentWidget(self.Help)
        
    def on_maintenance_sdbtn_clicked(self):
        self.CScreen_L.setText('> Maintenance')
        self.stackedWidget.setCurrentWidget(self.Main_1)
        
    def on_about_sdbtn_clicked(self):
        self.CScreen_L.setText('> About')
        self.stackedWidget.setCurrentWidget(self.about)