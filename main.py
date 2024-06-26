import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream
from PyQt5 import QtGui
from Screens.Login import LoginWindow
from Screens.ForgotPass.ForgotPass import ForgotPassWindow
from Screens.MainMenu import MainMenuWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Initialize Main Widget
        self.setWindowTitle("RANIL Inventory System")
        self.setMinimumWidth(1280)
        self.setMinimumHeight(720)

        # self.setWindowIcon(QtGui.QIcon(''))

        self.MainStack = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.MainStack)

        # Initialize Widgets for stack

        self.Login = LoginWindow()
        self.ForgotPass = ForgotPassWindow()
        self.MainMenu = MainMenuWindow()

        # Adding Widgets into MainStack
        self.MainStack.addWidget(self.Login)
        self.MainStack.addWidget(self.ForgotPass)
        self.MainStack.addWidget(self.MainMenu)

        # Connecting signals
        # Singals "TO" widgets

        self.Login.forgot.connect(
            lambda: self.MainStack.setCurrentWidget(self.ForgotPass)
        )
        self.Login.logsucc_admin.connect(self.Login_protocol)

        # Signals "BACK" to Widgets

        self.ForgotPass.back_btnsgl.connect(
            lambda: self.MainStack.setCurrentWidget(self.Login)
        )

        self.show()

    def Login_protocol(self):
        print("Login Attempt")
        self.MainStack.setCurrentWidget(self.MainMenu)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    Win = MainWindow()

    sys.exit(app.exec())
