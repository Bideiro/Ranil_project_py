import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QWidget


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("testing.ui", self)
        self.login.clicked.connect(self.gotologin)


    def gotologin(self):
        print("hello")


class regist(QDialog):
    def __init__(self):
        super(regist,self).__init__()
        loadUi(".ui")
app = QApplication(sys.argv)
welcome = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
try:
    sys.exit(app.exec())
except:
    print("Exit")


