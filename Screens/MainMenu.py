import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .MainMenu_ui import Ui_MainWindow

from .MainMenuScreens.Security.Security_1 import Security_1_Window
from .MainMenuScreens.Security.User_Information import User_Information_Window
from .MainMenuScreens.Security.User_Logs import User_Logs_Window

from .MainMenuScreens.Registration.Registration_1 import Registration_1_Window
from .MainMenuScreens.Registration.Registration_prod import Registration_prod_Window
from .MainMenuScreens.Registration.Registration_user import Registration_user_Window

from .MainMenuScreens.Reports.Reports_1 import Reports_1_Window

from .MainMenuScreens.Records.Records_1 import Records_1_Window

from .MainMenuScreens.Transaction.Transaction_1 import Transaction_1_Window

from .MainMenuScreens.About import AboutWindow

from Database.DBController import dbcont
from PyQt5 import QtWidgets, QtGui, QtCore
class MainMenuWindow( QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super(MainMenuWindow,self).__init__()
        self.setupUi(self)
        
        # Initializing Screens
        
        self.Secu_1 = Security_1_Window()
        self.User_Info = User_Information_Window()
        self.User_Logs = User_Logs_Window()
        
        self.Reg_1 = Registration_1_Window()
        self.Reg_prod = Registration_prod_Window()
        self.Reg_user = Registration_user_Window()
        
        self.Reports_1 = Reports_1_Window()
        
        self.Records_1 = Records_1_Window()
        
        self.Trans_1 = Transaction_1_Window()
        
        self.about = AboutWindow()
        
        # Adding Widgets into stack
        
        self.stackedWidget.addWidget(self.Secu_1)
        self.stackedWidget.addWidget(self.User_Info)
        self.stackedWidget.addWidget(self.User_Logs)
        
        self.stackedWidget.addWidget(self.Reg_1)
        self.stackedWidget.addWidget(self.Reg_prod)
        self.stackedWidget.addWidget(self.Reg_user)
        self.stackedWidget.addWidget(self.Reports_1)
        
        self.stackedWidget.addWidget(self.Records_1)
        
        self.stackedWidget.addWidget(self.Trans_1)
        
        self.stackedWidget.addWidget(self.about)
        
        # Sidebar visibility
        self.scrollArea.setVisible(False)
        self.menu_btn.toggled['bool'].connect(self.scrollArea.setVisible)
        
        # self.stackedWidget.addWidget(self.tetest)
        # self.stackedWidget.setCurrentWidget(self.tetest)
        
        # Signal Recievers
        
        # Security Buttons
        self.Secu_1.UInfo_btnsgl.connect(lambda: self.stackedWidget.setCurrentWidget(self.User_Info))
        self.Secu_1.ULogs_btnsgl.connect(lambda: self.stackedWidget.setCurrentWidget(self.User_Logs))
        
        # Registration Buttons
        self.Reg_1.prod_reg_btnsgl.connect(lambda: self.stackedWidget.setCurrentWidget(self.Reg_prod))
        self.Reg_1.user_reg_btnsgl.connect(lambda: self.stackedWidget.setCurrentWidget(self.Reg_user))
        
        self.Reg_prod.back_btnsgl.connect(lambda: self.stackedWidget.setCurrentWidget(self.Reg_1))
        self.Reg_user.back_btnsgl.connect(lambda: self.stackedWidget.setCurrentWidget(self.Reg_1))
        
        
        
    @pyqtSlot()
    # Functions changing windows
    
    def on_security_sdbtn_clicked(self):
        self.stackedWidget.setCurrentWidget(self.Secu_1)
        
    def on_help_sdbtn_clicked(self):
        self.stackedWidget.setCurrentWidget(self.about)
        
    def on_inventory_sdbtn_clicked(self):
        self.stackedWidget.setCurrentWidget(self.about)
        
    def on_maintenance_sdbtn_clicked(self):
        self.stackedWidget.setCurrentWidget(self.about)
        
    def on_records_sdbtn_clicked(self):
        self.stackedWidget.setCurrentWidget(self.Records_1)
        
    def on_registration_sdbtn_clicked(self):
        self.stackedWidget.setCurrentWidget(self.Reg_1)
        
    def on_reports_sdbtn_clicked(self):
        self.stackedWidget.setCurrentWidget(self.Reports_1)
        
    def on_sales_sdbtn_clicked(self):
        self.stackedWidget.setCurrentWidget(self.about)
        
    def on_about_sdbtn_clicked(self):
        self.stackedWidget.setCurrentWidget(self.about)
        
    def on_transaction_sdbtn_clicked(self):
        self.stackedWidget.setCurrentWidget(self.Trans_1)
        
        
    # Registration
    
    
    # @pyqtSlot()
    # def on_forgotpass_btn_clicked(self):
    #     print("forgot")
    #     self.forgot.emit()
        