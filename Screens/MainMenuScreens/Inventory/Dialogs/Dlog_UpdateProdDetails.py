
from PyQt5.QtWidgets import QMainWindow,QDialog, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream
from PyQt5 import QtWidgets, QtGui, QtCore

from .Dlog_UpdateProdDetails_ui import Ui_Dialog
from Dialogs.DLog_Alert import DLG_Alert
from Database.DBController import dbcont
from Database.App_functions import check_prod_validity

class DLG_Edit_Prod(QDialog, Ui_Dialog):
    
    update_btnsgl = QtCore.pyqtSignal()
    
    def __init__(self, Plist = None,parent = None):
        super().__init__(parent)
        
        self.setupUi(self)
        self.db = dbcont('admin',123456)
        
        self.Back_btn.clicked.connect(lambda: self.done(0))
        self.Update_btn.clicked.connect(self.init_update_prod)
        self.Disable_btn.clicked.connect(self.disable_prod)
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.Unit_CB.addItems(self.db.get_id_value(unit=True))
        self.Cat_CB.addItems(self.db.get_id_value(cate= True))
        
        self.PName_LE.setText(Plist[2])
        self.Desc_LE.setText(Plist[6])
        self.SPrice_LE.setText(Plist[3])
        self.Unit_CB.setCurrentIndex(self.db.get_id_value(value= Plist[7],unit=True))
        self.Cat_CB.setCurrentIndex(self.db.get_id_value(value= Plist[8],cate=True))
    def disable_prod(self):
        print('disable button clicked')
        
    def init_update_prod(self):
        funcmsg = check_prod_validity(Pname= self.PName_LE.text(), Utype= self.Unit_CB.currentIndex(),
                                    Sprice= self.SPrice_LE.text(), Cat= self.Cat_CB.currentIndex())
        if funcmsg != True:
            Dlg = DLG_Alert(msg= funcmsg)
            Dlg.exec()
        else:
            self.confirmed_update()
    
    def confirmed_update(self):
        Dlg = DLG_Alert()
        Dlg.exec()
        self.done(1)