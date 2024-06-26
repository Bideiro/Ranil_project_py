# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\dei\Documents\Programming\Ranil_project_py\Screens\MainMenuScreens\Sales\Sales.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(963, 663)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(".QWidget{\n"
"background-color: #F8F8F0;\n"
"}\n"
"#widget{\n"
"border: 2px solid #ABE27D;\n"
"}\n"
".QPushButton{\n"
"background-color: #096033;\n"
"border: 2px solid #ABE27D;\n"
"color: white\n"
"}\n"
"#Refresh_btn, #Search_btn, #Back_btn{\n"
"border: 2px solid;\n"
"}\n"
"#comboBox{\n"
"border : 1px solid gray;\n"
"color: black\n"
"}\n"
"#search_LE{\n"
"border : 1px solid gray;\n"
"color: black\n"
"}\n"
"#Sales_Table{\n"
"border : 2px solid #ABE27D;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("QPushButton {\n"
"    background-color: #096033;\n"
"    color: white;\n"
"\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.search_LE = QtWidgets.QLineEdit(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_LE.sizePolicy().hasHeightForWidth())
        self.search_LE.setSizePolicy(sizePolicy)
        self.search_LE.setMinimumSize(QtCore.QSize(400, 30))
        self.search_LE.setObjectName("search_LE")
        self.horizontalLayout_2.addWidget(self.search_LE)
        self.comboBox = QtWidgets.QComboBox(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.Search_btn = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Search_btn.sizePolicy().hasHeightForWidth())
        self.Search_btn.setSizePolicy(sizePolicy)
        self.Search_btn.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        self.Search_btn.setFont(font)
        self.Search_btn.setObjectName("Search_btn")
        self.horizontalLayout_2.addWidget(self.Search_btn)
        self.Refresh_btn = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Refresh_btn.sizePolicy().hasHeightForWidth())
        self.Refresh_btn.setSizePolicy(sizePolicy)
        self.Refresh_btn.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        self.Refresh_btn.setFont(font)
        self.Refresh_btn.setObjectName("Refresh_btn")
        self.horizontalLayout_2.addWidget(self.Refresh_btn)
        self.verticalLayout_4.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Sales_Table = QtWidgets.QTableWidget(self.widget_6)
        self.Sales_Table.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Sales_Table.sizePolicy().hasHeightForWidth())
        self.Sales_Table.setSizePolicy(sizePolicy)
        self.Sales_Table.setMinimumSize(QtCore.QSize(0, 500))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        self.Sales_Table.setFont(font)
        self.Sales_Table.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Sales_Table.setLineWidth(0)
        self.Sales_Table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Sales_Table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Sales_Table.setAlternatingRowColors(True)
        self.Sales_Table.setShowGrid(True)
        self.Sales_Table.setGridStyle(QtCore.Qt.SolidLine)
        self.Sales_Table.setObjectName("Sales_Table")
        self.Sales_Table.setColumnCount(7)
        self.Sales_Table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        item.setFont(font)
        item.setBackground(QtGui.QColor(42, 114, 222))
        self.Sales_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        item.setFont(font)
        self.Sales_Table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        item.setFont(font)
        self.Sales_Table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        item.setFont(font)
        self.Sales_Table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Sales_Table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Sales_Table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Sales_Table.setHorizontalHeaderItem(6, item)
        self.Sales_Table.horizontalHeader().setVisible(True)
        self.Sales_Table.horizontalHeader().setCascadingSectionResizes(True)
        self.Sales_Table.horizontalHeader().setHighlightSections(True)
        self.Sales_Table.horizontalHeader().setStretchLastSection(True)
        self.Sales_Table.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.Sales_Table)
        self.verticalLayout_4.addWidget(self.widget_6)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Back_btn = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Back_btn.sizePolicy().hasHeightForWidth())
        self.Back_btn.setSizePolicy(sizePolicy)
        self.Back_btn.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        self.Back_btn.setFont(font)
        self.Back_btn.setObjectName("Back_btn")
        self.horizontalLayout_3.addWidget(self.Back_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.dailySalesbtn = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dailySalesbtn.sizePolicy().hasHeightForWidth())
        self.dailySalesbtn.setSizePolicy(sizePolicy)
        self.dailySalesbtn.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        self.dailySalesbtn.setFont(font)
        self.dailySalesbtn.setObjectName("dailySalesbtn")
        self.horizontalLayout_3.addWidget(self.dailySalesbtn)
        self.monthlySalesbtn = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.monthlySalesbtn.sizePolicy().hasHeightForWidth())
        self.monthlySalesbtn.setSizePolicy(sizePolicy)
        self.monthlySalesbtn.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        self.monthlySalesbtn.setFont(font)
        self.monthlySalesbtn.setObjectName("monthlySalesbtn")
        self.horizontalLayout_3.addWidget(self.monthlySalesbtn)
        self.annualSalesbtn = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.annualSalesbtn.sizePolicy().hasHeightForWidth())
        self.annualSalesbtn.setSizePolicy(sizePolicy)
        self.annualSalesbtn.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        self.annualSalesbtn.setFont(font)
        self.annualSalesbtn.setObjectName("annualSalesbtn")
        self.horizontalLayout_3.addWidget(self.annualSalesbtn)
        self.verticalLayout_4.addWidget(self.widget_2)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_4.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SALES"))
        self.Search_btn.setText(_translate("MainWindow", "SEARCH"))
        self.Refresh_btn.setText(_translate("MainWindow", "REFRESH"))
        self.Sales_Table.setSortingEnabled(True)
        item = self.Sales_Table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date / Time"))
        item = self.Sales_Table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Reference Number"))
        item = self.Sales_Table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "User"))
        item = self.Sales_Table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Total Price"))
        item = self.Sales_Table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Paid Price"))
        item = self.Sales_Table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "GCashReference"))
        item = self.Sales_Table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "PaymentType"))
        self.Back_btn.setText(_translate("MainWindow", "BACK"))
        self.dailySalesbtn.setText(_translate("MainWindow", "DAILY SALES"))
        self.monthlySalesbtn.setText(_translate("MainWindow", "MONTHLY SALES"))
        self.annualSalesbtn.setText(_translate("MainWindow", "ANNUAL SALES"))
