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
    namelist = None
    selectedIndex = None
    
    def __init__(self):
        super(User_Information_Window,self).__init__()
        self.setupUi(self)
        
        self.db = dbcont('admin', '123456')
        self.back_btn.clicked.connect(self.createlist)
        
        self.createlist()
        self.accountList.clicked.connect(self.list_clicked)
        
        self.Edit_btn.clicked.connect(self.init_edit_protocol)
        
    def init_edit_protocol(self):
        
        if self.shown_user:
            Dlg = DLG_Edit_User( Ulist= self.shown_user)
            Dlg.exec()
            if Dlg.result() == 1:
                newUlist = [Dlg.ULevel_CB.currentIndex() ,Dlg.UName_LE.text(),
                        Dlg.FName_LE.text(), Dlg.LName_LE.text(),
                        Dlg.Sex_CB.currentIndex(), Dlg.Phono_LE.text().replace('+', '', 1),
                        Dlg.Email_LE.text(), Dlg.Pos_LE.text(),
                        Dlg.DHired_DE.date().toPyDate(), Dlg.BDate_DE.date().toPyDate(),
                        Dlg.Address_LE.text()]
                oldUlist = [self.shown_user[2], self.shown_user[4], self.shown_user[5]]
                self.db.update_user_protocol(oldUlist , newUlist)
                self.createlist()
                self.reset_values()
        else:
            Dlg = DLG_Alert(msg='Select a User first!')
            Dlg.exec()
            
        
    def createlist(self):
        self.accountList.clear()
        results = self.db.get_all_names()
        self.namelist  = results
        for result in results:
            compName = result[0] + ' ' + result[1]
            self.accountList.addItem(compName)
        self.accountList.update()

    def list_clicked(self):
        self.selectedIndex = self.accountList.currentIndex() #FIX
        selected_item = self.accountList.currentRow()# Get the currently selected item
        UserCreds = self.db.get_user_creds(Fname= self.namelist[selected_item][0], Lname= self.namelist[selected_item][1])
        
        print(UserCreds)
        self.Name_L.setText(self.accountList.currentItem().text())
        self.ULevel_L.setText(UserCreds[9])
        self.Email_L.setText(UserCreds[8])
        self.BDay_L.setText(UserCreds[11].strftime("%B %d, %Y"))
        self.Sex_L.setText(self.db.get_id_value(value= UserCreds[6], sex = True))
        self.Phono_L.setText(UserCreds[7])
        self.Pos_L.setText(UserCreds[9])
        self.HDate_L.setText(UserCreds[11].strftime("%B %d, %Y"))
        self.shown_user = UserCreds
        
        
    def reset_values(self):
        self.Name_L.setText('None')
        self.ULevel_L.setText('None')
        self.Email_L.setText('None')
        self.BDay_L.setText('None')
        self.Sex_L.setText('None')
        self.Phono_L.setText('None')
        self.Pos_L.setText('None')
        self.HDate_L.setText('None')
        
    def prev_window(self):
        self.back_btnsgl.emit()