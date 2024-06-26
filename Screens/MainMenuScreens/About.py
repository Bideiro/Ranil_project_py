import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .About_ui import Ui_MainWindow
from Dialogs.DLog_Alert import DLG_Alert


class AboutWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(AboutWindow,self).__init__()
        self.setupUi(self)

        
    def on_RJ_Email_clicked(self):
        Dlg = DLG_Alert(msg='email ni rheniel')
        Dlg.exec()
        
    def on_RJ_FB_clicked(self):
        Dlg = DLG_Alert(msg='Fb ni rheniel')
        Dlg.exec()
        
    def on_RJ_Phono_clicked(self):
        Dlg = DLG_Alert(msg='Phono ni rheniel')
        Dlg.exec()
        
    def on_DD_Email_clicked(self):
        Dlg = DLG_Alert(msg='email ni dei')
        Dlg.exec()
        
    def on_DD_FB_clicked(self):
        Dlg = DLG_Alert(msg='Fb ni dei')
        Dlg.exec()
        
    def on_DD_Phono_clicked(self):
        Dlg = DLG_Alert(msg='Phone ni dei')
        Dlg.exec()
        
    def on_FJ_Email_clicked(self):
        Dlg = DLG_Alert(msg='email ni che')
        Dlg.exec()
        
    def on_FJ_FB_clicked(self):
        Dlg = DLG_Alert(msg='Fb ni che')
        Dlg.exec()
        
    def on_FJ_Phono_clicked(self):
        Dlg = DLG_Alert(msg='Phone ni che')
        Dlg.exec()