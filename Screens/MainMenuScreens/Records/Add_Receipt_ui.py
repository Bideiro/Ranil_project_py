# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\dei\Documents\Programming\Ranil_project_py\Screens\MainMenuScreens\Records\Add_Receipt.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1052, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(".QWidget{\n"
"background-color: #F8F8F0;\n"
"}\n"
"#widget{\n"
"border : 2px solid #096033;\n"
"}\n"
"#widget_3, #widget_4, #widget_5{\n"
"border-left: 2px solid #096033;\n"
"border-right: 2px solid #096033;\n"
"}\n"
"#widget_5{\n"
"border-bottom: 2px solid #096033;\n"
"}\n"
"#widget_2{\n"
"background-color: #ABE27D;\n"
"border: 2px solid #096033;\n"
"}\n"
".QDateEdit{\n"
"background-color:rgba(0,0,0,0);\n"
"border : 2px solid #096033;\n"
"}\n"
"#PMethod_Cb, #RNumber_LE{\n"
"background-color:rgba(0,0,0,0);\n"
"border : 2px solid #096033;\n"
"}\n"
"#AProduct_btn, #RProduct_btn{\n"
"background-color:rgba(0,0,0,0);\n"
"}\n"
"QPushButton{\n"
"background-color: #096033;\n"
"color: white;\n"
"}\n"
"#Products_Table{\n"
"border : 1px solid black;\n"
"}\n"
"#Back_btn, #Finish_btn{\n"
"border: 2px solid;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setContentsMargins(-1, 12, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(682, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_5.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_7 = QtWidgets.QWidget(self.widget_3)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.ODate_DE = QtWidgets.QDateEdit(self.widget_7)
        self.ODate_DE.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        self.ODate_DE.setFont(font)
        self.ODate_DE.setCalendarPopup(True)
        self.ODate_DE.setTimeSpec(QtCore.Qt.LocalTime)
        self.ODate_DE.setObjectName("ODate_DE")
        self.verticalLayout.addWidget(self.ODate_DE)
        self.label_3 = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.RNumber_LE = QtWidgets.QLineEdit(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RNumber_LE.sizePolicy().hasHeightForWidth())
        self.RNumber_LE.setSizePolicy(sizePolicy)
        self.RNumber_LE.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        self.RNumber_LE.setFont(font)
        self.RNumber_LE.setObjectName("RNumber_LE")
        self.verticalLayout.addWidget(self.RNumber_LE)
        self.horizontalLayout_2.addWidget(self.widget_7)
        self.widget_8 = QtWidgets.QWidget(self.widget_3)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.label_5 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.DDate_DE = QtWidgets.QDateEdit(self.widget_8)
        self.DDate_DE.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        self.DDate_DE.setFont(font)
        self.DDate_DE.setCalendarPopup(True)
        self.DDate_DE.setObjectName("DDate_DE")
        self.verticalLayout_2.addWidget(self.DDate_DE)
        self.horizontalLayout_2.addWidget(self.widget_8)
        self.verticalLayout_5.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Products_Table = QtWidgets.QTableWidget(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        self.Products_Table.setFont(font)
        self.Products_Table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Products_Table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Products_Table.setAlternatingRowColors(True)
        self.Products_Table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.Products_Table.setObjectName("Products_Table")
        self.Products_Table.setColumnCount(5)
        self.Products_Table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(13)
        font.setBold(True)
        item.setFont(font)
        self.Products_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(13)
        font.setBold(True)
        item.setFont(font)
        self.Products_Table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(13)
        font.setBold(True)
        item.setFont(font)
        self.Products_Table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(13)
        font.setBold(True)
        item.setFont(font)
        self.Products_Table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(13)
        font.setBold(True)
        item.setFont(font)
        self.Products_Table.setHorizontalHeaderItem(4, item)
        self.Products_Table.horizontalHeader().setMinimumSectionSize(32)
        self.Products_Table.horizontalHeader().setStretchLastSection(True)
        self.Products_Table.verticalHeader().setVisible(False)
        self.Products_Table.verticalHeader().setMinimumSectionSize(24)
        self.horizontalLayout.addWidget(self.Products_Table)
        self.widget_6 = QtWidgets.QWidget(self.widget_4)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.AProduct_btn = QtWidgets.QPushButton(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        self.AProduct_btn.setFont(font)
        self.AProduct_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AProduct_btn.setIcon(icon)
        self.AProduct_btn.setIconSize(QtCore.QSize(50, 50))
        self.AProduct_btn.setObjectName("AProduct_btn")
        self.verticalLayout_4.addWidget(self.AProduct_btn)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem2)
        self.RProduct_btn = QtWidgets.QPushButton(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        self.RProduct_btn.setFont(font)
        self.RProduct_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/Icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RProduct_btn.setIcon(icon1)
        self.RProduct_btn.setIconSize(QtCore.QSize(50, 50))
        self.RProduct_btn.setObjectName("RProduct_btn")
        self.verticalLayout_4.addWidget(self.RProduct_btn)
        spacerItem3 = QtWidgets.QSpacerItem(20, 267, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout.addWidget(self.widget_6)
        self.verticalLayout_5.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setContentsMargins(20, -1, 20, 20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Back_btn = QtWidgets.QPushButton(self.widget_5)
        self.Back_btn.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(15)
        font.setBold(True)
        self.Back_btn.setFont(font)
        self.Back_btn.setObjectName("Back_btn")
        self.horizontalLayout_3.addWidget(self.Back_btn)
        spacerItem4 = QtWidgets.QSpacerItem(623, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.Finish_btn = QtWidgets.QPushButton(self.widget_5)
        self.Finish_btn.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(15)
        font.setBold(True)
        self.Finish_btn.setFont(font)
        self.Finish_btn.setObjectName("Finish_btn")
        self.horizontalLayout_3.addWidget(self.Finish_btn)
        self.verticalLayout_5.addWidget(self.widget_5)
        self.verticalLayout_3.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SUPPLIER RECEIPT"))
        self.label_2.setText(_translate("MainWindow", "Order Date:"))
        self.label_3.setText(_translate("MainWindow", "Receipt Number:"))
        self.label_5.setText(_translate("MainWindow", "Delivery Date:"))
        self.Products_Table.setSortingEnabled(True)
        item = self.Products_Table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product ID"))
        item = self.Products_Table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.Products_Table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Cost Price"))
        item = self.Products_Table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.Products_Table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Expiration Date"))
        self.Back_btn.setText(_translate("MainWindow", "BACK"))
        self.Finish_btn.setText(_translate("MainWindow", "FINISH"))
import assets.All_In_Resource_rc
