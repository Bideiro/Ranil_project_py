# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\dei\Documents\Programming\Ranil_project_py\Screens\MainMenuScreens\Reports\Inventory_Report.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 596)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(".QWidget{\n"
"background-color: #F8F8F0;\n"
"}\n"
".QPushButton{\n"
"background-color: #096033;\n"
"border: 2px solid;\n"
"color: white\n"
"}\n"
".QDateEdit{\n"
"border : 1px solid gray;\n"
"color: black\n"
"}\n"
"#Sales_Table{\n"
"border : 2px solid #ABE27D;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("QPushButton {\n"
"    background-color: #096033;\n"
"    color: white;\n"
"\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setStyleSheet("QPushButton {\n"
"    background-color: #096033;\n"
"    color: white;\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.widget_2)
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
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioButton = QtWidgets.QRadioButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_4.addWidget(self.radioButton)
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.FDate_DE = QtWidgets.QDateEdit(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FDate_DE.sizePolicy().hasHeightForWidth())
        self.FDate_DE.setSizePolicy(sizePolicy)
        self.FDate_DE.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        self.FDate_DE.setFont(font)
        self.FDate_DE.setCalendarPopup(True)
        self.FDate_DE.setObjectName("FDate_DE")
        self.horizontalLayout_4.addWidget(self.FDate_DE)
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.TDate_DE = QtWidgets.QDateEdit(self.widget_3)
        self.TDate_DE.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TDate_DE.sizePolicy().hasHeightForWidth())
        self.TDate_DE.setSizePolicy(sizePolicy)
        self.TDate_DE.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        self.TDate_DE.setFont(font)
        self.TDate_DE.setCalendarPopup(True)
        self.TDate_DE.setObjectName("TDate_DE")
        self.horizontalLayout_4.addWidget(self.TDate_DE)
        self.horizontalLayout_3.addWidget(self.widget_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.Search_btn = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Search_btn.sizePolicy().hasHeightForWidth())
        self.Search_btn.setSizePolicy(sizePolicy)
        self.Search_btn.setMinimumSize(QtCore.QSize(100, 30))
        self.Search_btn.setSizeIncrement(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        self.Search_btn.setFont(font)
        self.Search_btn.setObjectName("Search_btn")
        self.horizontalLayout_3.addWidget(self.Search_btn)
        self.Refresh_btn = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Refresh_btn.sizePolicy().hasHeightForWidth())
        self.Refresh_btn.setSizePolicy(sizePolicy)
        self.Refresh_btn.setMinimumSize(QtCore.QSize(100, 30))
        self.Refresh_btn.setSizeIncrement(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        self.Refresh_btn.setFont(font)
        self.Refresh_btn.setObjectName("Refresh_btn")
        self.horizontalLayout_3.addWidget(self.Refresh_btn)
        self.verticalLayout.addWidget(self.widget_2)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(False)
        self.tableWidget.setFont(font)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.generateBtn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generateBtn.sizePolicy().hasHeightForWidth())
        self.generateBtn.setSizePolicy(sizePolicy)
        self.generateBtn.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        self.generateBtn.setFont(font)
        self.generateBtn.setObjectName("generateBtn")
        self.horizontalLayout_2.addWidget(self.generateBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.radioButton.clicked['bool'].connect(self.TDate_DE.setEnabled) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "INVENTORY REPORTS"))
        self.radioButton.setText(_translate("MainWindow", "ENABLE DATE RANGE"))
        self.label_2.setText(_translate("MainWindow", "FROM"))
        self.label_3.setText(_translate("MainWindow", "TO"))
        self.Search_btn.setText(_translate("MainWindow", "SEARCH"))
        self.Refresh_btn.setText(_translate("MainWindow", "REFRESH"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Product ID"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Date"))
        self.pushButton_2.setText(_translate("MainWindow", "BACK"))
        self.generateBtn.setText(_translate("MainWindow", "GENERATE PDF"))
