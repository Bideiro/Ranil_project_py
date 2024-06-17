from PyQt5.QtWidgets import QMainWindow

from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

import datetime

from Database.DBController import dbcont

from .Dialogs.DLog_UpdateUserDetails import DLG_Edit_User
from Dialogs.DLog_Alert import DLG_Alert

from .User_Information_ui import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
class User_Information_Window(QMainWindow, Ui_MainWindow):
    back_btnsgl = QtCore.pyqtSignal()
    
    shown_user = None
    
    def __init__(self):
        super(User_Information_Window,self).__init__()
        self.setupUi(self)
        
        self.db = dbcont('admin', '123456')
        self.back_btn.clicked.connect(self.prev_window)
        
        self.createlist()
        self.accountList.clicked.connect(self.list_clicked)
        
        self.Edit_btn.clicked.connect(self.init_edit_protocol)
        
    def init_edit_protocol(self):
        
        if self.shown_user:
            Dlg = DLG_Edit_User( Ulist= self.shown_user)
            Dlg.exec()
            
        else:
            Dlg = DLG_Alert(msg='Select a User first!')
            Dlg.exec()
        
        
        
    def createlist(self):
        results = self.db.get_all_names()
        for result in results:
            compName = result[0] + ' ' + result[1]
            self.accountList.addItem(compName)

    def list_clicked(self):
        selected_item = self.accountList.currentItem().text()  # Get the currently selected item
        FullName = selected_item.split()
        
        UserCreds = self.db.get_user_creds(Fname= FullName[0], Lname= [1])
        
        self.Name_L.setText(self.accountList.currentItem().text())
        self.ULevel_L.setText(UserCreds[9])
        self.Email_L.setText(UserCreds[8])
        self.BDay_L.setText(UserCreds[11].strftime("%B %d, %Y"))
        self.Sex_L.setText(self.db.get_id_value(value= UserCreds[6], sex = True))
        self.Phono_L.setText(UserCreds[7])
        self.Pos_L.setText(UserCreds[9])
        self.HDate_L.setText(UserCreds[11].strftime("%B %d, %Y"))
        
        self.shown_user = UserCreds
        
    def prev_window(self):
        self.back_btnsgl.emit()