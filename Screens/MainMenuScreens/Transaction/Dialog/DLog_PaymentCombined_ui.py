# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\dei\Documents\Programming\Ranil_project_py\Screens\MainMenuScreens\Transaction\Dialog\DLog_PaymentCombined.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(543, 367)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(Dialog)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        self.widget.setFont(font)
        self.widget.setStyleSheet("#widget{\n"
"background-color: #F8F8F0;\n"
"border: 3px solid #ABE27D;\n"
"}\n"
".QPushButton{\n"
"background-color: #096033;\n"
"border: 2px solid;\n"
"color: white\n"
"}\n"
".QLineEdit{\n"
"border : 2px solid #ABE27D;\n"
"background-color:rgba(0,0,0,0);\n"
"color: gray\n"
"}\n"
".QLabel{\n"
"color: black;\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setContentsMargins(50, -1, 50, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.Input_LE = QtWidgets.QLineEdit(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Input_LE.sizePolicy().hasHeightForWidth())
        self.Input_LE.setSizePolicy(sizePolicy)
        self.Input_LE.setMinimumSize(QtCore.QSize(25, 35))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(11)
        self.Input_LE.setFont(font)
        self.Input_LE.setObjectName("Input_LE")
        self.verticalLayout_4.addWidget(self.Input_LE)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setContentsMargins(50, -1, 50, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(18)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.Input3_LE = QtWidgets.QLineEdit(self.widget_5)
        self.Input3_LE.setMinimumSize(QtCore.QSize(25, 35))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(11)
        self.Input3_LE.setFont(font)
        self.Input3_LE.setObjectName("Input3_LE")
        self.verticalLayout_3.addWidget(self.Input3_LE)
        self.verticalLayout.addWidget(self.widget_5)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setContentsMargins(50, -1, 50, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(18)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.Input2_LE = QtWidgets.QLineEdit(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Input2_LE.sizePolicy().hasHeightForWidth())
        self.Input2_LE.setSizePolicy(sizePolicy)
        self.Input2_LE.setMinimumSize(QtCore.QSize(25, 35))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(11)
        self.Input2_LE.setFont(font)
        self.Input2_LE.setMaxLength(30)
        self.Input2_LE.setObjectName("Input2_LE")
        self.verticalLayout_5.addWidget(self.Input2_LE)
        self.verticalLayout.addWidget(self.widget_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ok_btn = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok_btn.sizePolicy().hasHeightForWidth())
        self.ok_btn.setSizePolicy(sizePolicy)
        self.ok_btn.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(14)
        font.setBold(True)
        self.ok_btn.setFont(font)
        self.ok_btn.setObjectName("ok_btn")
        self.horizontalLayout.addWidget(self.ok_btn)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout_2.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "INPUT AMOUNT PAID IN CASH"))
        self.Input_LE.setPlaceholderText(_translate("Dialog", "Enter Amount Paid:"))
        self.label_3.setText(_translate("Dialog", "INPUT AMOUNT PAID IN GCASH"))
        self.Input3_LE.setPlaceholderText(_translate("Dialog", "Enter Amount Paid:"))
        self.label_2.setText(_translate("Dialog", "INPUT GCASH REFERENCE NUMBER"))
        self.Input2_LE.setPlaceholderText(_translate("Dialog", "Reference Number:"))
        self.ok_btn.setText(_translate("Dialog", "OK"))
