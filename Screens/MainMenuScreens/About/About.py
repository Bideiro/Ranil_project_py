import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream, QUrl
from PyQt5.QtGui import QDesktopServices

from .About_ui import Ui_MainWindow
from Dialogs.DLog_Alert import DLG_Alert

class AboutWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(AboutWindow, self).__init__()
        self.setupUi(self)
        
        # Connect the button to the function that opens the PDF
        self.UManual_btn.clicked.connect(self.open_pdf)

    def open_pdf(self):
        # Use QDesktopServices to open the PDF file
        pdf_path = QUrl.fromLocalFile('sample-user-manual.pdf')
        QDesktopServices.openUrl(pdf_path)
