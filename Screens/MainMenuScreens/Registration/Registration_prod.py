import sys
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream
from PyQt5.QtGui import QIntValidator

from .Registration_prod_ui import Ui_MainWindow
from .Dlog_tempalert import DLGsucc
from Database.DBController import dbcont


from PyQt5 import QtWidgets, QtGui, QtCore
class Registration_prod_Window(QMainWindow, Ui_MainWindow):

    back_btnsgl = QtCore.pyqtSignal()
    
    def __init__(self):
        super(Registration_prod_Window,self).__init__()
        self.setupUi(self)
        
        self.back_btn.clicked.connect(self.prev_window)
        self.reg_btn.clicked.connect(self.init_prod_reg_protocol)
        
        self.onlyInt = QIntValidator()
        self.Quan_LE.setValidator(self.onlyInt)
        self.CPrice_LE.setValidator(self.onlyInt)
        self.SPrice_LE.setValidator(self.onlyInt)
        
    def prev_window(self):
        self.back_btnsgl.emit()
        
    def init_prod_reg_protocol(self):
        
        db = dbcont("root","password")
        
        db.reg_prod_protocol(Pname= self.PName_LE.text(), Sprice=self.SPrice_LE.text(),
                            Edate=self.EDate_DE.date().toPyDate(),Cprice= self.CPrice_LE.text(),
                            quantity=self.Quan_LE.text(),desc=self.desc_LE.text()
                            )
        
        dlg = DLGsucc(self)
        dlg.exec()
        self.back_btnsgl.emit()