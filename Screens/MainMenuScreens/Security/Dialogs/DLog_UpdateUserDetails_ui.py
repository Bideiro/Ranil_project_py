# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\dei\Documents\Programming\Ranil_projecy_py\Screens\MainMenuScreens\Security\Dialogs\DLog_UpdateUserDetails.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(895, 534)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setStyleSheet("#widget{\n"
"background-color: #F8F8F0;\n"
"border: 2px solid #096033;\n"
"}\n"
".QLabel ,.QPushButton, .QComboBox ,.QLineEdit{\n"
"    font: 700 12pt \"DM Sans\";\n"
"}\n"
".QComboBox, .QLineEdit, .QDateEdit\n"
"{\n"
"border : 2px solid #096033;\n"
"background-color:rgba(0,0,0,0);\n"
"}\n"
".QPushButton{\n"
"background-color: #096033;\n"
"color: white;\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setStyleSheet("#widget_2{\n"
"background-color: #ABE27D;\n"
"border: 2px solid #096033;\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgba(0,0,0,0);")
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.verticalLayout_5.addWidget(self.widget_2)
        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.widget_7)
        self.widget_3.setStyleSheet(".QComboBox\n"
"{\n"
"border : 2px solid #096033;\n"
"}\n"
".QLineEdit{\n"
"border : 2px solid #096033;\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.FName_LE = QtWidgets.QLineEdit(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FName_LE.sizePolicy().hasHeightForWidth())
        self.FName_LE.setSizePolicy(sizePolicy)
        self.FName_LE.setMinimumSize(QtCore.QSize(25, 35))
        self.FName_LE.setText("")
        self.FName_LE.setObjectName("FName_LE")
        self.verticalLayout.addWidget(self.FName_LE)
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.UName_LE = QtWidgets.QLineEdit(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UName_LE.sizePolicy().hasHeightForWidth())
        self.UName_LE.setSizePolicy(sizePolicy)
        self.UName_LE.setMinimumSize(QtCore.QSize(25, 35))
        self.UName_LE.setText("")
        self.UName_LE.setObjectName("UName_LE")
        self.verticalLayout.addWidget(self.UName_LE)
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.ULevel_CB = QtWidgets.QComboBox(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ULevel_CB.sizePolicy().hasHeightForWidth())
        self.ULevel_CB.setSizePolicy(sizePolicy)
        self.ULevel_CB.setMinimumSize(QtCore.QSize(25, 35))
        self.ULevel_CB.setObjectName("ULevel_CB")
        self.verticalLayout.addWidget(self.ULevel_CB)
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.Sex_CB = QtWidgets.QComboBox(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Sex_CB.sizePolicy().hasHeightForWidth())
        self.Sex_CB.setSizePolicy(sizePolicy)
        self.Sex_CB.setMinimumSize(QtCore.QSize(25, 35))
        self.Sex_CB.setObjectName("Sex_CB")
        self.verticalLayout.addWidget(self.Sex_CB)
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.Phono_LE = QtWidgets.QLineEdit(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Phono_LE.sizePolicy().hasHeightForWidth())
        self.Phono_LE.setSizePolicy(sizePolicy)
        self.Phono_LE.setMinimumSize(QtCore.QSize(25, 35))
        self.Phono_LE.setText("")
        self.Phono_LE.setObjectName("Phono_LE")
        self.verticalLayout.addWidget(self.Phono_LE)
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget_7)
        self.widget_4.setStyleSheet(".QComboBox\n"
"{\n"
"border : 2px solid #096033;\n"
"}\n"
".QLineEdit{\n"
"border : 2px solid #096033;\n"
"}\n"
".QDateEdit{\n"
"border: 2px solid #096033;\n"
"}")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.widget_4)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.LName_LE = QtWidgets.QLineEdit(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LName_LE.sizePolicy().hasHeightForWidth())
        self.LName_LE.setSizePolicy(sizePolicy)
        self.LName_LE.setMinimumSize(QtCore.QSize(25, 35))
        self.LName_LE.setObjectName("LName_LE")
        self.verticalLayout_2.addWidget(self.LName_LE)
        self.label_8 = QtWidgets.QLabel(self.widget_4)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.Email_LE = QtWidgets.QLineEdit(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Email_LE.sizePolicy().hasHeightForWidth())
        self.Email_LE.setSizePolicy(sizePolicy)
        self.Email_LE.setMinimumSize(QtCore.QSize(25, 35))
        self.Email_LE.setObjectName("Email_LE")
        self.verticalLayout_2.addWidget(self.Email_LE)
        self.label_9 = QtWidgets.QLabel(self.widget_4)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.BDate_DE = QtWidgets.QDateEdit(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BDate_DE.sizePolicy().hasHeightForWidth())
        self.BDate_DE.setSizePolicy(sizePolicy)
        self.BDate_DE.setMinimumSize(QtCore.QSize(25, 35))
        self.BDate_DE.setDateTime(QtCore.QDateTime(QtCore.QDate(2024, 6, 7), QtCore.QTime(0, 0, 0)))
        self.BDate_DE.setCalendarPopup(True)
        self.BDate_DE.setCurrentSectionIndex(0)
        self.BDate_DE.setDate(QtCore.QDate(2024, 6, 7))
        self.BDate_DE.setObjectName("BDate_DE")
        self.verticalLayout_2.addWidget(self.BDate_DE)
        self.label_10 = QtWidgets.QLabel(self.widget_4)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.Pos_LE = QtWidgets.QLineEdit(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pos_LE.sizePolicy().hasHeightForWidth())
        self.Pos_LE.setSizePolicy(sizePolicy)
        self.Pos_LE.setMinimumSize(QtCore.QSize(25, 35))
        self.Pos_LE.setText("")
        self.Pos_LE.setObjectName("Pos_LE")
        self.verticalLayout_2.addWidget(self.Pos_LE)
        self.label_11 = QtWidgets.QLabel(self.widget_4)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.DHired_DE = QtWidgets.QDateEdit(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DHired_DE.sizePolicy().hasHeightForWidth())
        self.DHired_DE.setSizePolicy(sizePolicy)
        self.DHired_DE.setMinimumSize(QtCore.QSize(25, 35))
        self.DHired_DE.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.DHired_DE.setSpecialValueText("")
        self.DHired_DE.setCalendarPopup(True)
        self.DHired_DE.setObjectName("DHired_DE")
        self.verticalLayout_2.addWidget(self.DHired_DE)
        self.horizontalLayout_2.addWidget(self.widget_4)
        self.verticalLayout_5.addWidget(self.widget_7)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_12 = QtWidgets.QLabel(self.widget_5)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.Address_LE = QtWidgets.QLineEdit(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Address_LE.sizePolicy().hasHeightForWidth())
        self.Address_LE.setSizePolicy(sizePolicy)
        self.Address_LE.setMinimumSize(QtCore.QSize(0, 35))
        self.Address_LE.setText("")
        self.Address_LE.setObjectName("Address_LE")
        self.verticalLayout_3.addWidget(self.Address_LE)
        self.verticalLayout_5.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back_btn = QtWidgets.QPushButton(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_btn.sizePolicy().hasHeightForWidth())
        self.back_btn.setSizePolicy(sizePolicy)
        self.back_btn.setMinimumSize(QtCore.QSize(75, 35))
        self.back_btn.setObjectName("back_btn")
        self.horizontalLayout.addWidget(self.back_btn)
        spacerItem = QtWidgets.QSpacerItem(647, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.update_btn = QtWidgets.QPushButton(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_btn.sizePolicy().hasHeightForWidth())
        self.update_btn.setSizePolicy(sizePolicy)
        self.update_btn.setMinimumSize(QtCore.QSize(150, 35))
        self.update_btn.setObjectName("update_btn")
        self.horizontalLayout.addWidget(self.update_btn)
        self.verticalLayout_5.addWidget(self.widget_6)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Account Details"))
        self.label_2.setText(_translate("Dialog", "FIRST NAME:"))
        self.label_3.setText(_translate("Dialog", "USERNAME:"))
        self.label_4.setText(_translate("Dialog", "LEVEL OF ACCESS:"))
        self.label_5.setText(_translate("Dialog", "SEX:"))
        self.label_6.setText(_translate("Dialog", "PHONE NUMBER:"))
        self.label_7.setText(_translate("Dialog", "LAST NAME:"))
        self.label_8.setText(_translate("Dialog", "EMAIL:"))
        self.label_9.setText(_translate("Dialog", "BIRTH DATE:"))
        self.BDate_DE.setDisplayFormat(_translate("Dialog", "dd-mm-yyyy"))
        self.label_10.setText(_translate("Dialog", "POSITION:"))
        self.label_11.setText(_translate("Dialog", "DATE HIRED:"))
        self.DHired_DE.setDisplayFormat(_translate("Dialog", "dd-mm-yyyy"))
        self.label_12.setText(_translate("Dialog", "ADDRESS"))
        self.back_btn.setText(_translate("Dialog", "BACK"))
        self.update_btn.setText(_translate("Dialog", "SAVE CHANGES"))
