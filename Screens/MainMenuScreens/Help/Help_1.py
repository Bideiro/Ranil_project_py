import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream, QUrl
from PyQt5.QtGui import QDesktopServices

from .Help_1_ui import Ui_MainWindow

class HelpWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(HelpWindow, self).__init__()
        self.setupUi(self)
        self.Faqs_btn.clicked.connect(self.open_Faqs)
        self.UManual_btn.clicked.connect(self.open_UMan)

    def open_UMan(self):
        pdf_path = QUrl.fromLocalFile('Ranils-Poultry-Shop-Users-Manual.pdf')
        QDesktopServices.openUrl(pdf_path)
        
    def open_Faqs(self):
        pdf_path = QUrl.fromLocalFile('Ranils-Poultry-Shop-FAQs.pdf')
        QDesktopServices.openUrl(pdf_path)
