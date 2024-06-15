import sys
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream
from PyQt5.QtGui import QIntValidator

from .Registration_prod_ui import Ui_MainWindow
from .Dlog_tempalert import DLGsucc
from Database.DBController import *


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
        self.CType_CB.addItems(self.db.get_cate_types())
        self.UType_CB.addItems(self.db.get_unit_types())
        
        
    def prev_window(self):
        self.back_btnsgl.emit()
        
    def init_prod_reg_protocol(self):
        
        
        self.db.reg_prod_protocol(Pname = self.PName_LE.text(), Sprice=self.SPrice_LE.text(),
                            Utype= self.UType_CB.currentIndex(),Ctype= self.CType_CB.currentIndex(),
                            desc=self.desc_LE.text()
                            )
        
        dlg = DLGsucc(self)
        dlg.exec()
        self.back_btnsgl.emit()