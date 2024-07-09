import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream, QUrl
from PyQt5.QtGui import QDesktopServices

# Import the UI class
from .About_type2_ui import Ui_MainWindow
from Dialogs.DLog_Alert import DLG_Alert

class AboutWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(AboutWindow, self).__init__()
        self.setupUi(self)
        
    # Connect the buttons to their respective methods
        self.facebook_btn.clicked.connect(self.open_facebook)
        self.Email_btn.clicked.connect(self.open_email)
        self.Phone_btn.clicked.connect(self.open_phone)

    @pyqtSlot()
    def open_facebook(self):
        url = QUrl("https://www.facebook.com/profile.php?id=100066981633258")
        QDesktopServices.openUrl(url)

    @pyqtSlot()
    def open_email(self):
        email_address = "mailto:ma.rhonna.villanueva@gmail.com"
        QDesktopServices.openUrl(QUrl(email_address))

    @pyqtSlot()
    def open_phone(self):
        phone_number = "tel:0951 297 4169"
        QDesktopServices.openUrl(QUrl(phone_number))
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AboutWindow()
    window.show()
    sys.exit(app.exec_())
