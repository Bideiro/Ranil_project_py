from PyQt5.QtWidgets import QMainWindow, QLineEdit, QGraphicsDropShadowEffect
from PyQt5.QtGui import QIntValidator, QColor

from .Login_ui import Ui_MainWindow
from Database.DBController import dbcont
from Database.User_Manager import UserMana
from Dialogs.DLog_Alert import DLG_Alert
from PyQt5 import QtCore
class LoginWindow(QMainWindow, Ui_MainWindow):

    logsucc_emp = QtCore.pyqtSignal()
    logsucc_admin = QtCore.pyqtSignal()
    forgot = QtCore.pyqtSignal()
    
    User = UserMana()
    mydb = dbcont()
    
    def __init__(self):
        super(LoginWindow,self).__init__()
        self.setupUi(self)
        self.userLE.setFocus()
        self.onlyInt = QIntValidator()
        self.passwordLE.setMaxLength(6)
        self.passwordLE.setValidator(self.onlyInt)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(5)
        shadow.setYOffset(5)
        shadow.setColor(QColor(9, 96, 51))
        self.label.setGraphicsEffect(shadow)
        
        
        self.SPass_RB.toggled.connect(self.change_echo)
        self.login_btn.clicked.connect(self.init_login)
        self.forgotpass_btn.clicked.connect(lambda: self.forgot.emit())
        
    def change_echo(self):
        if self.SPass_RB.isChecked():
            self.passwordLE.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.passwordLE.setEchoMode(QLineEdit.EchoMode.Password)
        
    def init_login(self):
        if self.mydb.login(User= self.userLE.text(), passwd= self.passwordLE.text()):
            if self.User.Level == 0:
                self.logsucc_admin.emit()
            else:
                self.logsucc_emp.emit()
        else:
            Dlg = DLG_Alert(msg='Invalid Username or Password!')
            Dlg.exec()