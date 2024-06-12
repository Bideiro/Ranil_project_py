import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream
from PyQt5 import QtGui
from Screens.Login import LoginWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.MainStack = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.MainStack)
        
        self.Login = LoginWindow()
        
        self.MainStack.addWidget(self.Login)
        self.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    Win = MainWindow()

    sys.exit(app.exec())
