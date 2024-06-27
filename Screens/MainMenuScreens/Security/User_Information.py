from PyQt5.QtWidgets import QMainWindow

from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

import datetime

from Database.DBController import dbcont
from Database.User_Manager import UserMana

from .Dialogs.DLog_UpdateUserDetails import DLG_Edit_User
from Dialogs.DLog_Alert import DLG_Alert

from .User_Information_ui import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
class User_Information_Window(QMainWindow, Ui_MainWindow):
    back_btnsgl = QtCore.pyqtSignal()
    
    User = UserMana()
    db = dbcont()
    
    shown_user = None
    namelist = None
    selectedIndex = None
    
    def __init__(self):
        super(User_Information_Window,self).__init__()
        self.setupUi(self)

        self.createlist()
        

        self.back_btn.clicked.connect(self.prev_window)
        self.accountList.clicked.connect(self.list_clicked)
        
        self.Edit_btn.clicked.connect(self.init_edit_protocol)
        
    def set_CU_details(self):
        self.CULevel_L.setText(self.db.get_id_value(id= self.User.Level, level=True))
        self.CUName_L.setText(self.User.User)
        
    def init_edit_protocol(self):
        
        if self.shown_user:
            Dlg = DLG_Edit_User( Ulist= self.shown_user)
            Dlg.exec()
            if Dlg.result() == 1:
                newUlist = [Dlg.ULevel_CB.currentIndex() ,self.db._create_rid(id= self.shown_user[0],typeID= Dlg.ULevel_CB.currentIndex(),user= True),
                        Dlg.UName_LE.text(), Dlg.FName_LE.text(), Dlg.LName_LE.text(),
                        Dlg.Sex_CB.currentIndex(), Dlg.Phono_LE.text().replace('+', '', 1),
                        Dlg.Email_LE.text(), Dlg.Pos_LE.text(),
                        Dlg.DHired_DE.date().toPyDate(), Dlg.BDate_DE.date().toPyDate(),
                        Dlg.Address_LE.text()]
                UID = [self.shown_user[0]]
                print(self.shown_user[0])
                self.db.update_user_protocol(UID , newUlist)
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
        self.ULevel_L.setText(self.db.get_id_value(id=UserCreds[1],level=True))
        self.Email_L.setText(UserCreds[9])
        self.BDay_L.setText(UserCreds[12].strftime("%B %d, %Y"))
        self.Sex_L.setText(self.db.get_id_value(id= UserCreds[7], sex = True))
        self.Phono_L.setText(UserCreds[8])
        self.Pos_L.setText(UserCreds[10])
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