# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\dei\Documents\Programming\Ranil_project_py\Screens\MainMenuScreens\Records\Dialog\DLog_Receipt_Reprint.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(492, 722)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setStyleSheet(".QWidget{\n"
"background-color: #F8F8F0;\n"
"}\n"
"\n"
"#widget{\n"
"border: 1px solid black;\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Inconsolata")
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Inconsolata")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_4.addWidget(self.widget_3)
        self.verticalLayout_5.addWidget(self.widget_2)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("Inconsolata")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.verticalLayout_5.addWidget(self.widget_4)
        self.widget_10 = QtWidgets.QWidget(self.widget)
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.DateTime_L = QtWidgets.QLabel(self.widget_10)
        self.DateTime_L.setObjectName("DateTime_L")
        self.verticalLayout_2.addWidget(self.DateTime_L)
        self.widget_19 = QtWidgets.QWidget(self.widget_10)
        self.widget_19.setObjectName("widget_19")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_19)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_17 = QtWidgets.QLabel(self.widget_19)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_5.addWidget(self.label_17)
        self.UName_L = QtWidgets.QLabel(self.widget_19)
        self.UName_L.setObjectName("UName_L")
        self.horizontalLayout_5.addWidget(self.UName_L)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.widget_19)
        self.widget_20 = QtWidgets.QWidget(self.widget_10)
        self.widget_20.setObjectName("widget_20")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_20)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_18 = QtWidgets.QLabel(self.widget_20)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_9.addWidget(self.label_18)
        self.ReceiptNo_L = QtWidgets.QLabel(self.widget_20)
        self.ReceiptNo_L.setObjectName("ReceiptNo_L")
        self.horizontalLayout_9.addWidget(self.ReceiptNo_L)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.widget_20)
        self.verticalLayout_5.addWidget(self.widget_10)
        self.widget_15 = QtWidgets.QWidget(self.widget)
        self.widget_15.setObjectName("widget_15")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_15)
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.widget_15)
        font = QtGui.QFont()
        font.setFamily("Inconsolata")
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.label_8 = QtWidgets.QLabel(self.widget_15)
        font = QtGui.QFont()
        font.setFamily("Inconsolata")
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(self.widget_15)
        font = QtGui.QFont()
        font.setFamily("Inconsolata")
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.label_13 = QtWidgets.QLabel(self.widget_15)
        font = QtGui.QFont()
        font.setFamily("Inconsolata")
        font.setBold(True)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.label_13)
        self.verticalLayout_5.addWidget(self.widget_15)
        self.ProdList_w = QtWidgets.QWidget(self.widget)
        self.ProdList_w.setObjectName("ProdList_w")
        self.verticalLayout_5.addWidget(self.ProdList_w)
        self.widget_17 = QtWidgets.QWidget(self.widget)
        self.widget_17.setObjectName("widget_17")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget_17)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_7 = QtWidgets.QLabel(self.widget_17)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_11.addWidget(self.label_7)
        self.verticalLayout_5.addWidget(self.widget_17)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Inconsolata")
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.TotalPrice_L = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Inconsolata")
        font.setPointSize(15)
        self.TotalPrice_L.setFont(font)
        self.TotalPrice_L.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TotalPrice_L.setObjectName("TotalPrice_L")
        self.horizontalLayout_3.addWidget(self.TotalPrice_L)
        self.verticalLayout_5.addWidget(self.widget_6)
        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.PMethod_L = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setFamily("Inconsolata")
        font.setPointSize(13)
        self.PMethod_L.setFont(font)
        self.PMethod_L.setObjectName("PMethod_L")
        self.horizontalLayout_4.addWidget(self.PMethod_L)
        self.APaid_L = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setFamily("Inconsolata")
        font.setPointSize(13)
        self.APaid_L.setFont(font)
        self.APaid_L.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.APaid_L.setObjectName("APaid_L")
        self.horizontalLayout_4.addWidget(self.APaid_L)
        self.verticalLayout_5.addWidget(self.widget_7)
        self.widget_16 = QtWidgets.QWidget(self.widget)
        self.widget_16.setObjectName("widget_16")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_16)
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_14 = QtWidgets.QLabel(self.widget_16)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_8.addWidget(self.label_14)
        self.INumber_L = QtWidgets.QLabel(self.widget_16)
        self.INumber_L.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.INumber_L.setObjectName("INumber_L")
        self.horizontalLayout_8.addWidget(self.INumber_L)
        self.verticalLayout_5.addWidget(self.widget_16)
        self.widget_18 = QtWidgets.QWidget(self.widget)
        self.widget_18.setObjectName("widget_18")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.widget_18)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_5 = QtWidgets.QLabel(self.widget_18)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_12.addWidget(self.label_5)
        self.verticalLayout_5.addWidget(self.widget_18)
        self.widget_8 = QtWidgets.QWidget(self.widget)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 12)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setFamily("Inconsolata")
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.GCRef_L = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setFamily("Inconsolata")
        font.setPointSize(13)
        self.GCRef_L.setFont(font)
        self.GCRef_L.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.GCRef_L.setObjectName("GCRef_L")
        self.horizontalLayout_6.addWidget(self.GCRef_L)
        self.verticalLayout_5.addWidget(self.widget_8)
        self.widget_9 = QtWidgets.QWidget(self.widget)
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_10.setContentsMargins(-1, 0, -1, 12)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_11 = QtWidgets.QLabel(self.widget_9)
        font = QtGui.QFont()
        font.setFamily("Inconsolata")
        font.setPointSize(13)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_10.addWidget(self.label_11)
        self.label_16 = QtWidgets.QLabel(self.widget_9)
        font = QtGui.QFont()
        font.setFamily("Inconsolata")
        font.setBold(True)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_10.addWidget(self.label_16)
        self.verticalLayout_5.addWidget(self.widget_9)
        self.verticalLayout_6.addWidget(self.widget)
        self.widget_5 = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_5.setStyleSheet(".QPushButton{\n"
"    background-color: rgb(9, 96, 51);\n"
"    color: rgb(255, 255, 255);\n"
"    border:4px solid rgb(171, 226, 125);\n"
"}")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Print_btn = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Print_btn.sizePolicy().hasHeightForWidth())
        self.Print_btn.setSizePolicy(sizePolicy)
        self.Print_btn.setMinimumSize(QtCore.QSize(25, 35))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(13)
        font.setBold(True)
        self.Print_btn.setFont(font)
        self.Print_btn.setObjectName("Print_btn")
        self.verticalLayout_8.addWidget(self.Print_btn)
        self.verticalLayout_6.addWidget(self.widget_5)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Ranil\'s Poultry Shop"))
        self.label_2.setText(_translate("Dialog", "#6, Rizal Avenue, Balite, Montalban (Rodriguez) Rizal"))
        self.label_4.setText(_translate("Dialog", "SALES RECEIPT"))
        self.DateTime_L.setText(_translate("Dialog", "DATE/TIME"))
        self.label_17.setText(_translate("Dialog", "Cashier: "))
        self.UName_L.setText(_translate("Dialog", "Name"))
        self.label_18.setText(_translate("Dialog", "Receipt No.:"))
        self.ReceiptNo_L.setText(_translate("Dialog", "Numbers"))
        self.label_9.setText(_translate("Dialog", "Item"))
        self.label_8.setText(_translate("Dialog", "Price"))
        self.label_3.setText(_translate("Dialog", "Qty"))
        self.label_13.setText(_translate("Dialog", "Amount"))
        self.label_7.setText(_translate("Dialog", "----------------------------------------------------"))
        self.label_6.setText(_translate("Dialog", "TOTAL:"))
        self.TotalPrice_L.setText(_translate("Dialog", "TextLabel"))
        self.PMethod_L.setText(_translate("Dialog", "PAYMENT TYPE"))
        self.APaid_L.setText(_translate("Dialog", "TextLabel"))
        self.label_14.setText(_translate("Dialog", "Number of Item/s:"))
        self.INumber_L.setText(_translate("Dialog", "TextLabel"))
        self.label_5.setText(_translate("Dialog", "----------------------------------------------------"))
        self.label_10.setText(_translate("Dialog", "Reference Number: "))
        self.GCRef_L.setText(_translate("Dialog", "TextLabel"))
        self.label_11.setText(_translate("Dialog", "THANK YOU!"))
        self.label_16.setText(_translate("Dialog", "THIS DOCUMENT OF NOT VALID FOR CLAIM OF INPUT TAX"))
        self.Print_btn.setText(_translate("Dialog", "PRINT RECEIPT"))
