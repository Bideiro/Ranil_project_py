# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\dei\Documents\Programming\Ranil_project_py\Screens\MainMenuScreens\Inventory\Inventory.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(".QWidget{\n"
"background-color: #F8F8F0;\n"
"}\n"
"\n"
".QPushButton{\n"
"background-color: #096033;\n"
"border: 2px solid;\n"
"color: white\n"
"}\n"
"#search_LE{\n"
"border : 1px solid gray;\n"
"color: black\n"
"}\n"
"#Product_Table{\n"
"border : 2px solid #ABE27D;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setContentsMargins(12, -1, -1, -1)
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
        self.search_LE = QtWidgets.QLineEdit(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_LE.sizePolicy().hasHeightForWidth())
        self.search_LE.setSizePolicy(sizePolicy)
        self.search_LE.setMinimumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        self.search_LE.setFont(font)
        self.search_LE.setObjectName("search_LE")
        self.horizontalLayout_3.addWidget(self.search_LE)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.Search_btn = QtWidgets.QPushButton(self.widget_2)
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
        self.horizontalLayout_3.addWidget(self.Search_btn)
        self.Refresh_btn = QtWidgets.QPushButton(self.widget_2)
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
        self.horizontalLayout_3.addWidget(self.Refresh_btn)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Product_Table = QtWidgets.QTableWidget(self.widget_4)
        self.Product_Table.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Product_Table.sizePolicy().hasHeightForWidth())
        self.Product_Table.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(False)
        self.Product_Table.setFont(font)
        self.Product_Table.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Product_Table.setLineWidth(0)
        self.Product_Table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Product_Table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Product_Table.setAlternatingRowColors(True)
        self.Product_Table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.Product_Table.setShowGrid(True)
        self.Product_Table.setGridStyle(QtCore.Qt.SolidLine)
        self.Product_Table.setObjectName("Product_Table")
        self.Product_Table.setColumnCount(9)
        self.Product_Table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        item.setFont(font)
        item.setBackground(QtGui.QColor(42, 114, 222))
        self.Product_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        item.setFont(font)
        self.Product_Table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        item.setFont(font)
        self.Product_Table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        item.setFont(font)
        self.Product_Table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        item.setFont(font)
        self.Product_Table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        item.setFont(font)
        self.Product_Table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        item.setFont(font)
        self.Product_Table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        item.setFont(font)
        self.Product_Table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        item.setFont(font)
        self.Product_Table.setHorizontalHeaderItem(8, item)
        self.Product_Table.horizontalHeader().setVisible(True)
        self.Product_Table.horizontalHeader().setCascadingSectionResizes(True)
        self.Product_Table.horizontalHeader().setHighlightSections(True)
        self.Product_Table.horizontalHeader().setMinimumSectionSize(32)
        self.Product_Table.horizontalHeader().setStretchLastSection(True)
        self.Product_Table.verticalHeader().setVisible(False)
        self.Product_Table.verticalHeader().setMinimumSectionSize(24)
        self.Product_Table.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_4.addWidget(self.Product_Table)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "INVENTORY"))
        self.search_LE.setPlaceholderText(_translate("MainWindow", "Search:"))
        self.Search_btn.setText(_translate("MainWindow", "SEARCH"))
        self.Refresh_btn.setText(_translate("MainWindow", "REFRESH"))
        self.Product_Table.setSortingEnabled(True)
        item = self.Product_Table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product ID"))
        item = self.Product_Table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.Product_Table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Category"))
        item = self.Product_Table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Unit Type"))
        item = self.Product_Table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Selling Price"))
        item = self.Product_Table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Expiration Date"))
        item = self.Product_Table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Stock"))
        item = self.Product_Table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Description"))
        item = self.Product_Table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Status"))
