
from PyQt5.QtWidgets import QMainWindow,QDialog, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream
from PyQt5 import QtWidgets, QtGui, QtCore

from .DLog_UpdateProdDetails_ui import Ui_Dialog
from Dialogs.DLog_Alert import DLG_Alert
from Database.DBController import dbcont
from Database.App_functions import check_prod_validity

class DLG_Edit_Prod(QDialog, Ui_Dialog):
    
    update_btnsgl = QtCore.pyqtSignal()
    db = dbcont()
    
    def __init__(self,isEnabled, Plist = None,parent = None):
        super().__init__(parent)
        
        self.setupUi(self)
        
        self.plist = Plist
        self.switch_inputs(active= isEnabled)
        
        self.Back_btn.clicked.connect(lambda: self.done(0))
        self.Update_btn.clicked.connect(self.init_update_prod)
        self.Disable_btn.clicked.connect(self.switch_in_db)
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.Unit_CB.addItems(self.db.get_unittype(all=True))
        self.Cat_CB.addItems(self.db.get_cate(all= True))
        
        self.PName_LE.setText(Plist[1])
        self.Desc_LE.setText(Plist[7])
        self.SPrice_LE.setText(Plist[4])
        self.Unit_CB.setCurrentIndex(self.db.get_unittype(value= Plist[3]))
        self.Cat_CB.setCurrentIndex(self.db.get_cate(value= Plist[2]))
        
    def init_update_prod(self):
        
        if self.db.get_status(RPID=self.plist[0]) == 0:
            dlg =DLG_Alert('Cant edit a disabled product!')
            dlg.exec()
        else:
            funcmsg = check_prod_validity(Pname= self.PName_LE.text(), Utype= self.Unit_CB.currentIndex(),
                                        Sprice= self.SPrice_LE.text(), Cat= self.Cat_CB.currentIndex())
            if funcmsg != True:
                Dlg = DLG_Alert(msg= funcmsg)
                Dlg.exec()
            else:
                self.confirmed_update()
                
            
    def switch_in_db(self):
        active = self.db.get_status(RPID=self.plist[0])
        if active == 1:
            self.db.get_status(RPID= self.plist[0], status= 0)
        else:
            self.db.get_status(RPID= self.plist[0], status= 1)
        curr = self.db.get_status(RPID=self.plist[0])
        self.switch_inputs(curr)
    
    def switch_inputs(self, active):
        if active == 0:
            self.Disable_btn.setText('ENABLE')
            self.PName_LE.setEnabled(False)
            self.Desc_LE.setEnabled(False)
            self.SPrice_LE.setEnabled(False)
            self.Unit_CB.setEnabled(False)
            self.Cat_CB.setEnabled(False)
        else:
            self.Disable_btn.setText('DISABLE')
            self.PName_LE.setEnabled(True)
            self.Desc_LE.setEnabled(True)
            self.SPrice_LE.setEnabled(True)
            self.Unit_CB.setEnabled(True)
            self.Cat_CB.setEnabled(True)
        
    def confirmed_update(self):
        Dlg = DLG_Alert()
        Dlg.exec()
        self.done(1)