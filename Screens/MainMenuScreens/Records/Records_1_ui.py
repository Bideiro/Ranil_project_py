# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\dei\Documents\Programming\Ranil_projecy_py\Screens\MainMenuScreens\Records\Records_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(810, 607)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(".QPushButton{\n"
"    background-color: rgb(9, 96, 51);\n"
"    color: rgb(255, 255, 255);\n"
"    border:4px solid rgb(171, 226, 125);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 164, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.receipts_btn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.receipts_btn.sizePolicy().hasHeightForWidth())
        self.receipts_btn.setSizePolicy(sizePolicy)
        self.receipts_btn.setMaximumSize(QtCore.QSize(16777215, 74))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(12)
        font.setBold(True)
        self.receipts_btn.setFont(font)
        self.receipts_btn.setObjectName("receipts_btn")
        self.verticalLayout.addWidget(self.receipts_btn)
        spacerItem2 = QtWidgets.QSpacerItem(20, 75, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.trans_btn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trans_btn.sizePolicy().hasHeightForWidth())
        self.trans_btn.setSizePolicy(sizePolicy)
        self.trans_btn.setMinimumSize(QtCore.QSize(350, 0))
        self.trans_btn.setMaximumSize(QtCore.QSize(16777215, 75))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(12)
        font.setBold(True)
        self.trans_btn.setFont(font)
        self.trans_btn.setObjectName("trans_btn")
        self.verticalLayout.addWidget(self.trans_btn)
        spacerItem3 = QtWidgets.QSpacerItem(20, 164, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout.addWidget(self.widget)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.receipts_btn.setText(_translate("MainWindow", "SUPPLIER RECEIPTS RECORDS"))
        self.trans_btn.setText(_translate("MainWindow", "TRANSACTION RECEIPT RECORDS"))
