# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\dei\Documents\Programming\Ranil_project_py\Screens\MainMenuScreens\Registration\Dialog\DLog_NewUnit.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(513, 240)
        Dialog.setStyleSheet("#widget{\n"
"background-color: #ABE27D;\n"
"border: 3px solid black;\n"
"}\n"
".QPushButton{\n"
"background-color: #096033;\n"
"border: 3px solid;\n"
"color: white\n"
"}\n"
".QLineEdit{\n"
"border : 2px solid #096033;\n"
"background-color: #F8F8F0;\n"
"color: black\n"
"}\n"
".QLabel{\n"
"color: black;\n"
"}")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(14)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.widget_4)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Input_LE = QtWidgets.QLineEdit(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Input_LE.sizePolicy().hasHeightForWidth())
        self.Input_LE.setSizePolicy(sizePolicy)
        self.Input_LE.setMinimumSize(QtCore.QSize(25, 35))
        self.Input_LE.setObjectName("Input_LE")
        self.verticalLayout_3.addWidget(self.Input_LE)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back_btn = QtWidgets.QPushButton(self.widget_2)
        self.back_btn.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(14)
        font.setBold(True)
        self.back_btn.setFont(font)
        self.back_btn.setObjectName("back_btn")
        self.horizontalLayout.addWidget(self.back_btn)
        spacerItem = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ok_btn = QtWidgets.QPushButton(self.widget_2)
        self.ok_btn.setMinimumSize(QtCore.QSize(30, 40))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(14)
        font.setBold(True)
        self.ok_btn.setFont(font)
        self.ok_btn.setObjectName("ok_btn")
        self.horizontalLayout.addWidget(self.ok_btn)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout_4.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "ENTER NEW UNIT TYPE:"))
        self.label_2.setText(_translate("Dialog", "Ex. Liters, pack, kg, piece"))
        self.back_btn.setText(_translate("Dialog", "BACK"))
        self.ok_btn.setText(_translate("Dialog", "OK"))
