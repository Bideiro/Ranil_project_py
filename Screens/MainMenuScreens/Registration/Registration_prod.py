import sys
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream
from PyQt5.QtGui import QIntValidator

from .Registration_prod_ui import Ui_MainWindow
from Dialogs.DLog_Alert import DLG_Alert
from Database.DBController import dbcont
from Database.App_functions import check_prod_validity


from PyQt5 import QtWidgets, QtGui, QtCore
class Registration_prod_Window(QMainWindow, Ui_MainWindow):

    back_btnsgl = QtCore.pyqtSignal()
        
    
    def __init__(self):
        super(Registration_prod_Window,self).__init__()
        self.setupUi(self)
        
        self.db = dbcont("root","password")
        
        self.back_btn.clicked.connect(self.prev_window)
        self.reg_btn.clicked.connect(self.init_prod_reg_protocol)
        
        # self.reg_btn.clicked.connect(self.test)
        
        self.onlyInt = QIntValidator()
        self.SPrice_LE.setValidator(self.onlyInt)
        self.CType_CB.addItems(self.db.get_cate(all=True))
        self.UType_CB.addItems(self.db.get_unittype(all=True))
        
    def prev_window(self):
        self.back_btnsgl.emit()
        
    def init_prod_reg_protocol(self):

        funcmsg = check_prod_validity(Pname= self.PName_LE.text(), Utype= self.UType_CB.currentIndex(),
                                    Sprice= self.SPrice_LE.text(), Cat= self.CType_CB.currentIndex())
        if funcmsg == True:
            self.confirmed_reg()
        else:
            errdlg = DLG_Alert(msg= funcmsg)
            errdlg.exec()
        
    def confirmed_reg(self):
        
        self.db.reg_prod_protocol(Pname = self.PName_LE.text(), Sprice=self.SPrice_LE.text(),
                            Utype= self.UType_CB.currentIndex(),Ctype= self.CType_CB.currentIndex(),
                            desc=self.desc_LE.text()
                            )
        
        dlg = DLG_Alert()
        dlg.exec()
        self.back_btnsgl.emit()
