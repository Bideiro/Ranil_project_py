import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream, QUrl
from PyQt5.QtGui import QDesktopServices

from .About_ui import Ui_MainWindow
from Dialogs.DLog_Alert import DLG_Alert


class AboutWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(AboutWindow,self).__init__()
        self.setupUi(self)

    @pyqtSlot()
    def on_RJ_Email_clicked(self):
        QDesktopServices.openUrl(QUrl('mailto:qrjfdamasco@tip.edu.ph'))
    @pyqtSlot()
    def on_RJ_FB_clicked(self):
        QDesktopServices.openUrl(QUrl('https://www.facebook.com/Rheinioool'))
    @pyqtSlot()
    def on_RJ_Phono_clicked(self):
        QDesktopServices.openUrl(QUrl('tel:+639154974346'))
    @pyqtSlot()
    def on_DD_Email_clicked(self):
        QDesktopServices.openUrl(QUrl('mailto:qd-deocampo@tip.edu.ph'))
        
    def on_DD_FB_clicked(self):
        QDesktopServices.openUrl(QUrl('https://www.facebook.com/deighro.deocampo'))
        
    def on_DD_Phono_clicked(self):
        QDesktopServices.openUrl(QUrl('tel:+639081391924'))
        
    def on_FJ_Email_clicked(self):
        QDesktopServices.openUrl(QUrl('mailto:qfnmacam@tip.edu.ph'))
        
    def on_FJ_FB_clicked(self):
        QDesktopServices.openUrl(QUrl('https://www.facebook.com/franchesca.macam'))
        
    def on_FJ_Phono_clicked(self):
        QDesktopServices.openUrl(QUrl('tel:+639493075834'))