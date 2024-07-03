import sys
from PyQt5 import QtWidgets, QtGui

from Database.User_Manager import UserMana
from Screens.Login import LoginWindow
from Screens.ForgotPass.ForgotPass import ForgotPassWindow
from Screens.MainMenu import MainMenuWindow
from Screens.MainMenu_E import MainMenuWindow_E

class MainWindow(QtWidgets.QMainWindow):
    
    User = UserMana()
    def __init__(self):
        super(MainWindow, self).__init__()

        # Initialize Main Widget
        self.setWindowTitle("RANIL Inventory System")
        self.setMinimumWidth(1408)
        self.setMinimumHeight(792)

        self.setWindowIcon(QtGui.QIcon('assets\images\Ranil_ICON.png'))

        self.MainStack = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.MainStack)

        # Initialize Widgets for stack

        self.Login = LoginWindow()
        self.ForgotPass = ForgotPassWindow()
        self.MainMenu = MainMenuWindow()
        self.MainMenu_E = MainMenuWindow_E()

        # Adding Widgets into MainStack
        self.MainStack.addWidget(self.Login)
        self.MainStack.addWidget(self.ForgotPass)
        self.MainStack.addWidget(self.MainMenu)
        self.MainStack.addWidget(self.MainMenu_E)

        # Connecting signals
        # for resizing
        # self.MainMenu.resize_trig.connect(self.resize_app)
        
        
        self.MainMenu.log_out_btnsgl.connect(self.Log_out_protocol)
        self.MainMenu_E.log_out_btnsgl.connect(self.Log_out_protocol)
        # Singals "TO" widgets

        self.Login.forgot.connect(lambda: self.MainStack.setCurrentWidget(self.ForgotPass))
        self.Login.logsucc_admin.connect(self.handle_login_admin)
        self.Login.logsucc_emp.connect(self.handle_login_emp)

        # Signals "BACK" to Widgets

        self.ForgotPass.back_btnsgl.connect(lambda: self.MainStack.setCurrentWidget(self.Login))
        self.show()
        
    def handle_login_admin(self):
        self.MainMenu.User_L.setText('> ' + self.User.User)
        self.MainStack.setCurrentWidget(self.MainMenu)
        
    def handle_login_emp(self):
        self.MainMenu_E.User_L.setText('> ' + self.User.User)
        self.MainStack.setCurrentWidget(self.MainMenu_E)
        
    def Log_out_protocol(self):
        print('Logging Out')
        self.User.reset_UserMana()
        self.Login.userLE.clear()
        self.Login.passwordLE.clear()
        self.MainStack.setCurrentWidget(self.Login)
        
        
    def resize_app(self):
        currentWidget = self.MainStack.currentWidget()
        self.resize(currentWidget.minimumSizeHint())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    Win = MainWindow()

    sys.exit(app.exec())
