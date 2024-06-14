import sys
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .Registration_prod_ui import Ui_MainWindow

from PyQt5 import QtWidgets, QtGui, QtCore
class Registration_prod_Window(QMainWindow, Ui_MainWindow):

    back_btnsgl = QtCore.pyqtSignal()
    
    def __init__(self):
        super(Registration_prod_Window,self).__init__()
        self.setupUi(self)
        
        self.back_btn.clicked.connect(self.prev_window)
        # self.reg_btn.clicked.connect(self.confirm_pass)
        
    def prev_window(self):
        self.back_btnsgl.emit()
        
    