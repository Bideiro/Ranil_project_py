
from urllib.request import OpenerDirector
from PyQt5.QtWidgets import QMainWindow, QListWidget, QListWidgetItem
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
from Database.DBController import dbcont
from Database.User_Manager import UserMana

from .Dialogs.DLog_UpdateUserDetails import DLG_Edit_User
from Dialogs.DLog_Alert import DLG_Alert

from .User_Information_ui import Ui_MainWindow
from PyQt5 import QtCore
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
        
        self.PReset_w.setVisible(False)
        self.Disabled_w.setVisible(False)
        palette = self.accountList.palette()
        palette.setColor(QPalette.AlternateBase, QColor(238, 234, 224))
        self.accountList.setPalette(palette)
        
        self.accountList.itemClicked.connect(self.list_clicked)
        self.Edit_btn.clicked.connect(self.init_edit_protocol)
        
    
    def update_status(self, RUID):
        status = self.db.access_status_user(RUID= RUID)
        if status == 3:
            self.PReset_w.setVisible(True)
        elif status == 0:
            self.Disabled_w.setVisible(True)
        else:
            self.Disabled_w.setVisible(False)
            self.PReset_w.setVisible(False)
    
    def init_edit_protocol(self):
        if self.shown_user:
            Dlg = DLG_Edit_User( Ulist= self.shown_user)
            Dlg.disable_btnsgl.connect(lambda:print('hello'))
            Dlg.exec()
            if Dlg.result() == 1:
                newUlist = [Dlg.ULevel_CB.currentIndex(),
                            self.db._create_rid(id= self.shown_user[0], typeID= Dlg.ULevel_CB.currentIndex(),user= True), 
                            Dlg.UName_LE.text(),
                            Dlg.FName_LE.text(),
                            Dlg.LName_LE.text(),
                            Dlg.MName_LE.text(),
                            Dlg.Suffix_CB.currentIndex(),
                            Dlg.Sex_CB.currentIndex(),
                            Dlg.Phono_LE.text().replace('+', '', 1),
                            Dlg.Email_LE.text(),
                            Dlg.Pos_LE.text(),
                            Dlg.DHired_DE.date().toPyDate(),
                            Dlg.BDate_DE.date().toPyDate(),
                            Dlg.Address_LE.text(),
                            Dlg.Pass_LE.text()
                            ]
                UID = [self.shown_user[0]]
                self.db.update_user_protocol(UID , newUlist)
                self.createlist()
                self.reset_values()
            else:
                self.update_status(RUID= self.shown_user[2])
        else:
            Dlg = DLG_Alert(msg='Select a User first!')
            Dlg.exec()
        
    def createlist(self):
        self.accountList.clear()
        results = self.db.get_all_users()
        for result in results:
            if result[8] != 0:
                suffix = self.db.get_suffix(id= result[8])
            else:
                suffix = ''
            if result[7] == None or result[7] == '':
                whole_name = str(result[5]) + ' ' + str(result[6]) + ' ' + str(suffix)
            else:
                whole_name = str(result[5]) + ' ' + str(result[7]) + ' ' + str(result[6]) + ' ' + str(suffix)
                
            item = QListWidgetItem(whole_name)
            item.setData(Qt.UserRole + 1, result[2])
            
            self.accountList.addItem(item)
        self.accountList.update()

    def list_clicked(self, item):
        RUID = item.data(Qt.UserRole + 1)
        UserCreds = self.db.get_user_creds(RUID= RUID)
        self.UName_L.setText(UserCreds[3])
        self.Name_L.setText(self.accountList.currentItem().text())
        self.UID_L.setText(UserCreds[2])
        self.ULevel_L.setText(self.db.get_levels(id=UserCreds[1]))
        self.Email_L.setText(UserCreds[11])
        self.BDay_L.setText(UserCreds[14].strftime("%B %d, %Y"))
        self.Sex_L.setText(self.db.get_sex(id= UserCreds[9]))
        self.Phono_L.setText(UserCreds[10])
        self.Pos_L.setText(UserCreds[12])
        self.HDate_L.setText(UserCreds[13].strftime("%B %d, %Y"))
        
        # Setting user status alert
        
        if UserCreds[16] == 3:
            self.PReset_w.setVisible(True)
        elif UserCreds[16] == 0:
            self.Disabled_w.setVisible(True)
        else:
            self.Disabled_w.setVisible(False)
            self.PReset_w.setVisible(False)
            
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
        self.UID_L.setText('None')