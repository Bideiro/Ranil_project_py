import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream
from PyQt5 import QtGui
from Screens.Login import LoginWindow
from Screens.ForgotPass import ForgotPassWindow
from Screens.MainMenu import MainMenuWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # Initialize Main Widget
        self.setWindowTitle("RANIL Inventory System")
        
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
        
        self.Login.forgot.connect(self.to_forgot)
        self.Login.logsucc_admin.connect(self.to_mainmenu)
        
        # Signals "BACK" to Widgets
        
        self.ForgotPass.back.connect(self.return_login)
        
        
        self.show()
        
    # Functions "TO" Widgets
    
    def to_mainmenu(self):
        self.MainStack.setCurrentWidget(self.MainMenu)
        print()
    
    def to_forgot(self):
        self.MainStack.setCurrentWidget(self.ForgotPass)
        
        
    # Functions "BACK" to Widgets
        
    def return_login(self):
        self.MainStack.setCurrentWidget(self.Login)
        



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    Win = MainWindow()

    sys.exit(app.exec())
