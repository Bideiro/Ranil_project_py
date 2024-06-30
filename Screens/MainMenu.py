import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .MainMenu_ui import Ui_MainWindow

from .MainMenuScreens.Home import HomeWindow

from .MainMenuScreens.Security.Security_1 import Security_1_Window
from .MainMenuScreens.Security.User_Information import User_Information_Window
from .MainMenuScreens.Security.User_Logs import User_Logs_Window

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

from .MainMenuScreens.Maintenance.Maintenance_1 import Maintenance_Window

from .MainMenuScreens.About import AboutWindow

from Database.DBController import dbcont
from Database.User_Manager import UserMana
from PyQt5 import QtWidgets, QtGui, QtCore
class MainMenuWindow( QMainWindow, Ui_MainWindow):
    
    log_out_btnsgl = QtCore.pyqtSignal()
    User = UserMana()
    db = dbcont()
    
    def __init__(self):
        super(MainMenuWindow,self).__init__()
        self.setupUi(self)
        
        # Initializing Screens
        
        self.Home = HomeWindow()
        
        self.Secu_1 = Security_1_Window()
        self.User_Info = User_Information_Window()
        self.User_Logs = User_Logs_Window()
        
        self.Reg_1 = Registration_1_Window()
        self.Reg_prod = Registration_prod_Window()
        self.Reg_user = Registration_user_Window()
        
        self.Sales = Sales_Window()
        
        self.Trans_prod = Trans_Prod_Window()
        
        self.Inven = Inventory_Window()
        
        self.Records_1 = Records_1_Window()
        self.Supp_Receipts = Supp_Rec_Window()
        self.Add_Supp_Receipt = add_reciept_Window()
        self.Trans_Receipts = Trans_Rec_Window()
        
        self.Reports_1 = Reports_1_Window()
        
        self.Main_1 = Maintenance_Window()
        self.about = AboutWindow()
    
        
        # Adding Widgets into stack
        
        self.stackedWidget.addWidget(self.Home)
        
        self.stackedWidget.addWidget(self.Secu_1)
        self.stackedWidget.addWidget(self.User_Info)
        self.stackedWidget.addWidget(self.User_Logs)
        
        self.stackedWidget.addWidget(self.Reg_1)
        self.stackedWidget.addWidget(self.Reg_prod)
        self.stackedWidget.addWidget(self.Reg_user)
        
        self.stackedWidget.addWidget(self.Sales)
        
        self.stackedWidget.addWidget(self.Trans_prod)
        
        self.stackedWidget.addWidget(self.Inven)
        
        self.stackedWidget.addWidget(self.Records_1)
        self.stackedWidget.addWidget(self.Supp_Receipts)
        self.stackedWidget.addWidget(self.Add_Supp_Receipt)
        self.stackedWidget.addWidget(self.Trans_Receipts)
        
        self.stackedWidget.addWidget(self.Reports_1)
        
        self.stackedWidget.addWidget(self.Main_1)
        
        self.stackedWidget.addWidget(self.about)
        
        # Initializationg of Menu
        # Sidebar visibility
        self.scrollArea.setVisible(False)
        self.menu_btn.toggled['bool'].connect(self.scrollArea.setVisible)
        self.stackedWidget.setCurrentWidget(self.Home)
        
        # Signal Recievers
        # Security Buttons
        self.Secu_1.UInfo_btnsgl.connect(lambda: self.stackedWidget.setCurrentWidget(self.User_Info))
        self.Secu_1.ULogs_btnsgl.connect(lambda: self.stackedWidget.setCurrentWidget(self.User_Logs))
        
        self.User_Info.back_btnsgl.connect(lambda: self.stackedWidget.setCurrentWidget(self.Secu_1))
        
        # Registration Buttons
        self.Reg_1.prod_reg_btnsgl.connect(lambda: self.stackedWidget.setCurrentWidget(self.Reg_prod))
        self.Reg_1.user_reg_btnsgl.connect(lambda: self.stackedWidget.setCurrentWidget(self.Reg_user))
        
        self.Reg_prod.back_btnsgl.connect(lambda: self.stackedWidget.setCurrentWidget(self.Reg_1))
        self.Reg_user.back_btnsgl.connect(lambda: self.stackedWidget.setCurrentWidget(self.Reg_1))
        
        # Sales Buttons
        
        # Transaction Buttons
        
        
        # Records Buttons
        self.Records_1.SReciepts_btnsgl.connect(lambda: self.stackedWidget.setCurrentWidget(self.Supp_Receipts))
        self.Records_1.TReceipts_btnsgl.connect(lambda: self.stackedWidget.setCurrentWidget(self.Trans_Receipts))
        
        
        self.Supp_Receipts.Add_btnsgl.connect(lambda: self.stackedWidget.setCurrentWidget(self.Add_Supp_Receipt))
        self.Supp_Receipts.back_btnsgl.connect(lambda: self.stackedWidget.setCurrentWidget(self.Records_1))
        
        self.Trans_Receipts.back_btnsgl.connect(lambda: self.stackedWidget.setCurrentWidget(self.Records_1))
        
        # Reports Buttons
        
        # Help Buttons
        
        #Log Out
        self.log_out_sdbtn.clicked.connect(self.init_log_out)
        
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
        self.log_out_btnsgl.emit()
        
    
    
    @pyqtSlot()
    # Functions changing windows
    
    def on_security_sdbtn_clicked(self):
        self.User_Info.set_CU_details()
        self.stackedWidget.setCurrentWidget(self.Secu_1)
        
    def on_registration_sdbtn_clicked(self):
        self.stackedWidget.setCurrentWidget(self.Reg_1)
        
    def on_sales_sdbtn_clicked(self):
        self.stackedWidget.setCurrentWidget(self.Sales)
        
    def on_transaction_sdbtn_clicked(self):
        self.Trans_prod.reset_page()
        self.stackedWidget.setCurrentWidget(self.Trans_prod)
        
    def on_help_sdbtn_clicked(self):
        self.stackedWidget.setCurrentWidget(self.about)
        
    def on_inventory_sdbtn_clicked(self):
        self.Inven.set_tableElements()
        self.stackedWidget.setCurrentWidget(self.Inven)
        
        
    def on_records_sdbtn_clicked(self):
        self.stackedWidget.setCurrentWidget(self.Records_1)
        
    def on_reports_sdbtn_clicked(self):
        self.stackedWidget.setCurrentWidget(self.Reports_1)
        
    def on_maintenance_sdbtn_clicked(self):
        self.stackedWidget.setCurrentWidget(self.Main_1)
        
    def on_about_sdbtn_clicked(self):
        self.stackedWidget.setCurrentWidget(self.about)