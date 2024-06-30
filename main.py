import sys
from PyQt5 import QtWidgets

from Database.User_Manager import UserMana
from Screens.Login import LoginWindow
from Screens.ForgotPass.ForgotPass import ForgotPassWindow
from Screens.MainMenu import MainMenuWindow


class MainWindow(QtWidgets.QMainWindow):
    
    User = UserMana()
    def __init__(self):
        super(MainWindow, self).__init__()

        # Initialize Main Widget
        self.setWindowTitle("RANIL Inventory System")
        self.setMinimumWidth(1408)
        self.setMinimumHeight(792)

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
        
        self.MainMenu.log_out_btnsgl.connect(self.Log_out_protocol)
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
        
    def Log_out_protocol(self):
        self.User.reset_UserMana()
        self.Login.userLE.clear()
        self.Login.passwordLE.clear()
        self.MainStack.setCurrentWidget(self.Login)

    def Login_protocol(self):
        print("Login Attempt")
        self.MainStack.setCurrentWidget(self.MainMenu)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    Win = MainWindow()

    sys.exit(app.exec())
