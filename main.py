import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream
from PyQt5 import QtGui
from Login import LoginWindow

# class MainWindow(QWidget):
#     def __init__(self):
#         super(MainWindow, self).__init__()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    a = LoginWindow()

    sys.exit(app.exec())
