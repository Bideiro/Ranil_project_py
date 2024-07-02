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
        
        self.UManual_btn.clicked.connect(self.open_pdf)
        
        
    def open_pdf(self):
        file_name = 'User manual Samsung Galaxy S24 Ultra (English - 206 pages).pdf'  # Replace with your file name
        self.webview.setUrl(QUrl.fromLocalFile(file_name))
