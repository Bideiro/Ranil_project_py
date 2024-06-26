import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .Add_Receipt_ui import Ui_MainWindow
from .Dialog.DLog_Insert_prod import DLG_Insert_Prod

from PyQt5 import QtWidgets, QtGui, QtCore
class add_reciept_Window(QMainWindow, Ui_MainWindow):

    Add_btnsgl = QtCore.pyqtSignal()
    
    def __init__(self):
        super(add_reciept_Window,self).__init__()
        self.setupUi(self)
        
        
        
        
        self.AProduct_btn.clicked.connect(self.Dlg_prod)
    
    
    def Dlg_prod(self):
        
        Dlg = DLG_Insert_Prod()
        Dlg.exec()
        if Dlg.result == 1:
            
            
            pass
        
        else:
            print('cancelled')
        
        