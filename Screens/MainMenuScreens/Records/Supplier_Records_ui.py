# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\dei\Documents\Programming\Ranil_project_py\Screens\MainMenuScreens\Records\Supplier_Records.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1228, 623)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(".QWidget{\n"
"background-color: #F8F8F0\n"
"}\n"
"#widget{\n"
"border: 2px solid #ABE27D;\n"
"}\n"
"#search_LE{\n"
"border : 1px solid gray;\n"
"color: black\n"
"}\n"
".QPushButton{\n"
"background-color: #096033;\n"
"border: 2px solid;\n"
"color: white\n"
"}\n"
"#Add_btn{\n"
"background-color:rgba(0,0,0,0);\n"
"border: none\n"
"}\n"
".QTableWidget{\n"
"border: 1px solid black;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget)
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
        self.search_LE = QtWidgets.QLineEdit(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_LE.sizePolicy().hasHeightForWidth())
        self.search_LE.setSizePolicy(sizePolicy)
        self.search_LE.setMinimumSize(QtCore.QSize(500, 30))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        self.search_LE.setFont(font)
        self.search_LE.setObjectName("search_LE")
        self.horizontalLayout_3.addWidget(self.search_LE)
        spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.Search_btn = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Search_btn.sizePolicy().hasHeightForWidth())
        self.Search_btn.setSizePolicy(sizePolicy)
        self.Search_btn.setMinimumSize(QtCore.QSize(100, 10))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        self.Search_btn.setFont(font)
        self.Search_btn.setObjectName("Search_btn")
        self.horizontalLayout_3.addWidget(self.Search_btn)
        self.Refresh_btn = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Refresh_btn.sizePolicy().hasHeightForWidth())
        self.Refresh_btn.setSizePolicy(sizePolicy)
        self.Refresh_btn.setMinimumSize(QtCore.QSize(100, 10))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        self.Refresh_btn.setFont(font)
        self.Refresh_btn.setObjectName("Refresh_btn")
        self.horizontalLayout_3.addWidget(self.Refresh_btn)
        self.Delete_btn = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Delete_btn.sizePolicy().hasHeightForWidth())
        self.Delete_btn.setSizePolicy(sizePolicy)
        self.Delete_btn.setMinimumSize(QtCore.QSize(100, 10))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        self.Delete_btn.setFont(font)
        self.Delete_btn.setObjectName("Delete_btn")
        self.horizontalLayout_3.addWidget(self.Delete_btn)
        self.verticalLayout.addWidget(self.widget_2)
        self.SReceipts_Table = QtWidgets.QTableWidget(self.widget)
        self.SReceipts_Table.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("DM Sans 14pt ExtraBold")
        font.setBold(False)
        self.SReceipts_Table.setFont(font)
        self.SReceipts_Table.setFrameShadow(QtWidgets.QFrame.Plain)
        self.SReceipts_Table.setLineWidth(0)
        self.SReceipts_Table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.SReceipts_Table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.SReceipts_Table.setAlternatingRowColors(True)
        self.SReceipts_Table.setShowGrid(True)
        self.SReceipts_Table.setGridStyle(QtCore.Qt.SolidLine)
        self.SReceipts_Table.setObjectName("SReceipts_Table")
        self.SReceipts_Table.setColumnCount(8)
        self.SReceipts_Table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(13)
        font.setBold(True)
        item.setFont(font)
        self.SReceipts_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(13)
        font.setBold(True)
        item.setFont(font)
        self.SReceipts_Table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(13)
        font.setBold(True)
        item.setFont(font)
        self.SReceipts_Table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(13)
        font.setBold(True)
        item.setFont(font)
        self.SReceipts_Table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(13)
        font.setBold(True)
        item.setFont(font)
        self.SReceipts_Table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(13)
        font.setBold(True)
        item.setFont(font)
        self.SReceipts_Table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(13)
        font.setBold(True)
        item.setFont(font)
        self.SReceipts_Table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(13)
        font.setBold(True)
        item.setFont(font)
        self.SReceipts_Table.setHorizontalHeaderItem(7, item)
        self.SReceipts_Table.horizontalHeader().setVisible(True)
        self.SReceipts_Table.horizontalHeader().setCascadingSectionResizes(True)
        self.SReceipts_Table.horizontalHeader().setHighlightSections(True)
        self.SReceipts_Table.horizontalHeader().setMinimumSectionSize(32)
        self.SReceipts_Table.horizontalHeader().setStretchLastSection(True)
        self.SReceipts_Table.verticalHeader().setVisible(False)
        self.SReceipts_Table.verticalHeader().setMinimumSectionSize(24)
        self.verticalLayout.addWidget(self.SReceipts_Table)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Back_btn = QtWidgets.QPushButton(self.widget_3)
        self.Back_btn.setMinimumSize(QtCore.QSize(100, 40))
        self.Back_btn.setObjectName("Back_btn")
        self.horizontalLayout_2.addWidget(self.Back_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.Add_btn = QtWidgets.QPushButton(self.widget_3)
        self.Add_btn.setMinimumSize(QtCore.QSize(50, 50))
        self.Add_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Add_btn.setIcon(icon)
        self.Add_btn.setIconSize(QtCore.QSize(70, 70))
        self.Add_btn.setObjectName("Add_btn")
        self.horizontalLayout_2.addWidget(self.Add_btn)
        self.verticalLayout.addWidget(self.widget_3)
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SUPPLIER RECORDS"))
        self.Search_btn.setText(_translate("MainWindow", "SEARCH"))
        self.Refresh_btn.setText(_translate("MainWindow", "REFRESH"))
        self.Delete_btn.setText(_translate("MainWindow", "DISABLE"))
        self.SReceipts_Table.setSortingEnabled(True)
        item = self.SReceipts_Table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.SReceipts_Table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "User"))
        item = self.SReceipts_Table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Receipt Ref"))
        item = self.SReceipts_Table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Total Price"))
        item = self.SReceipts_Table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Payment Type"))
        item = self.SReceipts_Table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Order Date"))
        item = self.SReceipts_Table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Delivery Date"))
        item = self.SReceipts_Table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "GCash Reference"))
        self.Back_btn.setText(_translate("MainWindow", "BACK"))
import assets.All_In_Resource_rc
