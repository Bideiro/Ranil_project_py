# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\dei\Documents\Programming\Ranil_project_py\Screens\MainMenuScreens\Inventory\Dialogs\DLog_UpdateProdDetails.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(734, 507)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(720, 360))
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setStyleSheet("#widget{\n"
"background-color: #F8F8F0;\n"
"border: 2px solid #096033;\n"
"}\n"
".QComboBox, .QDateEdit, .QLineEdit\n"
"{\n"
"border : 2px solid #096033;\n"
"background-color:rgba(0,0,0,0);\n"
"}\n"
"#add_btn, #sub_btn{\n"
"background-color:rgba(0,0,0,0);\n"
"}\n"
"\n"
".QComboBox:disabled, .QDateEdit:disabled, .QLineEdit:disabled {\n"
"background-color: #ccc;\n"
"color: #666;\n"
"}\n"
"")
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 65))
        self.widget_2.setStyleSheet("#widget_2{\n"
"background-color: #ABE27D;\n"
"border: 2px solid #096033;\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgba(0,0,0,0);")
        self.label.setIndent(10)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_4.addWidget(self.widget_2)
        self.widget_16 = QtWidgets.QWidget(self.widget)
        self.widget_16.setObjectName("widget_16")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_16)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.widget_4 = QtWidgets.QWidget(self.widget_16)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_9 = QtWidgets.QWidget(self.widget_4)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.widget_9)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.verticalLayout_2.addWidget(self.widget_9)
        self.widget_8 = QtWidgets.QWidget(self.widget_4)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.verticalLayout_2.addWidget(self.widget_8)
        self.widget_10 = QtWidgets.QWidget(self.widget_4)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(self.widget_10)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.verticalLayout_2.addWidget(self.widget_10)
        self.widget_11 = QtWidgets.QWidget(self.widget_4)
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label_5 = QtWidgets.QLabel(self.widget_11)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.verticalLayout_2.addWidget(self.widget_11)
        self.widget_3 = QtWidgets.QWidget(self.widget_4)
        font = QtGui.QFont()
        font.setBold(True)
        self.widget_3.setFont(font)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.horizontalLayout_13.addWidget(self.widget_4)
        self.widget_15 = QtWidgets.QWidget(self.widget_16)
        self.widget_15.setObjectName("widget_15")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_5 = QtWidgets.QWidget(self.widget_15)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.PName_LE = QtWidgets.QLineEdit(self.widget_5)
        self.PName_LE.setEnabled(True)
        self.PName_LE.setMinimumSize(QtCore.QSize(25, 35))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        self.PName_LE.setFont(font)
        self.PName_LE.setObjectName("PName_LE")
        self.horizontalLayout_9.addWidget(self.PName_LE)
        self.verticalLayout_3.addWidget(self.widget_5)
        self.widget_7 = QtWidgets.QWidget(self.widget_15)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.Desc_LE = QtWidgets.QLineEdit(self.widget_7)
        self.Desc_LE.setMinimumSize(QtCore.QSize(25, 35))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        self.Desc_LE.setFont(font)
        self.Desc_LE.setObjectName("Desc_LE")
        self.horizontalLayout_8.addWidget(self.Desc_LE)
        self.verticalLayout_3.addWidget(self.widget_7)
        self.widget_12 = QtWidgets.QWidget(self.widget_15)
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.SPrice_LE = QtWidgets.QLineEdit(self.widget_12)
        self.SPrice_LE.setMinimumSize(QtCore.QSize(25, 35))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        self.SPrice_LE.setFont(font)
        self.SPrice_LE.setObjectName("SPrice_LE")
        self.horizontalLayout_12.addWidget(self.SPrice_LE)
        self.verticalLayout_3.addWidget(self.widget_12)
        self.widget_13 = QtWidgets.QWidget(self.widget_15)
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.Unit_CB = QtWidgets.QComboBox(self.widget_13)
        self.Unit_CB.setMinimumSize(QtCore.QSize(25, 35))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        self.Unit_CB.setFont(font)
        self.Unit_CB.setObjectName("Unit_CB")
        self.horizontalLayout_10.addWidget(self.Unit_CB)
        self.verticalLayout_3.addWidget(self.widget_13)
        self.widget_14 = QtWidgets.QWidget(self.widget_15)
        self.widget_14.setObjectName("widget_14")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_14)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.Cat_CB = QtWidgets.QComboBox(self.widget_14)
        self.Cat_CB.setMinimumSize(QtCore.QSize(25, 35))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        self.Cat_CB.setFont(font)
        self.Cat_CB.setObjectName("Cat_CB")
        self.horizontalLayout_11.addWidget(self.Cat_CB)
        self.verticalLayout_3.addWidget(self.widget_14)
        self.horizontalLayout_13.addWidget(self.widget_15)
        self.verticalLayout_4.addWidget(self.widget_16)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setStyleSheet(".QPushButton{\n"
"background-color: #096033;\n"
"color: white;\n"
"}")
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 30)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.Back_btn = QtWidgets.QPushButton(self.widget_6)
        self.Back_btn.setMinimumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(10)
        font.setBold(True)
        self.Back_btn.setFont(font)
        self.Back_btn.setObjectName("Back_btn")
        self.horizontalLayout_3.addWidget(self.Back_btn)
        spacerItem6 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.Disable_btn = QtWidgets.QPushButton(self.widget_6)
        self.Disable_btn.setMinimumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(10)
        font.setBold(True)
        self.Disable_btn.setFont(font)
        self.Disable_btn.setObjectName("Disable_btn")
        self.horizontalLayout_3.addWidget(self.Disable_btn)
        spacerItem7 = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.Update_btn = QtWidgets.QPushButton(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Update_btn.sizePolicy().hasHeightForWidth())
        self.Update_btn.setSizePolicy(sizePolicy)
        self.Update_btn.setMinimumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(10)
        font.setBold(True)
        self.Update_btn.setFont(font)
        self.Update_btn.setObjectName("Update_btn")
        self.horizontalLayout_3.addWidget(self.Update_btn)
        spacerItem8 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.verticalLayout_4.addWidget(self.widget_6)
        self.verticalLayout_5.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "EDIT PRODUCT"))
        self.label_3.setText(_translate("Dialog", "PRODUCT NAME:"))
        self.label_2.setText(_translate("Dialog", "DESCRIPTION:"))
        self.label_4.setText(_translate("Dialog", "SELLING PRICE:"))
        self.label_5.setText(_translate("Dialog", "UNIT TYPE:"))
        self.label_6.setText(_translate("Dialog", "CATEGORY:"))
        self.Back_btn.setText(_translate("Dialog", "BACK"))
        self.Disable_btn.setText(_translate("Dialog", "DISABLE"))
        self.Update_btn.setText(_translate("Dialog", "UPDATE"))
import assets.All_In_Resource_rc
