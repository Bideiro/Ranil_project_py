# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\dei\Documents\Programming\Ranil_project_py\Screens\MainMenu_E.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(893, 677)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    var w = window.innerWidth;\n"
"    var h = window.innerHeight;\n"
"    print(w)\n"
"    print(h)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("/*Nav Bar*/\n"
"#top_bar{\n"
"    background-color: #096033;\n"
"}\n"
"#menu_btn{\n"
"    border: 2px solid #096033;\n"
"    text-align: left;\n"
"    padding-left: 15px;\n"
"    background-color: #096033;\n"
"}\n"
"#menu_btn:checked, #menu_btn:toggled{\n"
"    background-color: white;\n"
"}\n"
"\n"
"/* Side Buttons */ \n"
"#about_sdbtn, #help_sdbtn ,#inventory_sdbtn, #maintenance_sdbtn, #records_sdbtn,#registration_sdbtn,#reports_sdbtn,#sales_sdbtn,#security_sdbtn,#transaction_sdbtn, #log_out_sdbtn{\n"
"    color: #096033;\n"
"    border: 3px solid #096033;\n"
"    text-align: left;\n"
"    padding: 10px 10px;\n"
"    background-color: white;\n"
"    margin: 0px;\n"
"}\n"
"#about_sdbtn:hover, #help_sdbtn:hover ,#inventory_sdbtn:hover, #maintenance_sdbtn:hover, #records_sdbtn:hover,#registration_sdbtn:hover,#reports_sdbtn:hover,#sales_sdbtn:hover,#security_sdbtn:hover,#transaction_sdbtn:hover, #log_out_sdbtn:hover {\n"
"    background-color: #096033;\n"
"    color: white;\n"
"}\n"
"#about_sdbtn:checked, #help_sdbtn:checked,#inventory_sdbtn:checked, #maintenance_sdbtn:checked, #records_sdbtn:checked,#registration_sdbtn:checked,#reports_sdbtn:checked,#sales_sdbtn:checked,#security_sdbtn:checked,#transaction_sdbtn:checked , #log_out_sdbtn:checked{\n"
"    background-color: #096033;\n"
"    color: white;\n"
"}\n"
"#nav_text, #CScreen_L, #User_L {\n"
"    color: white;\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.top_bar = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_bar.sizePolicy().hasHeightForWidth())
        self.top_bar.setSizePolicy(sizePolicy)
        self.top_bar.setMinimumSize(QtCore.QSize(0, 65))
        self.top_bar.setStyleSheet("")
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.menu_btn = QtWidgets.QPushButton(self.top_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_btn.sizePolicy().hasHeightForWidth())
        self.menu_btn.setSizePolicy(sizePolicy)
        self.menu_btn.setMinimumSize(QtCore.QSize(60, 25))
        self.menu_btn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.menu_btn.setStyleSheet("")
        self.menu_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/option white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/option green.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.menu_btn.setIcon(icon)
        self.menu_btn.setIconSize(QtCore.QSize(25, 25))
        self.menu_btn.setCheckable(True)
        self.menu_btn.setChecked(False)
        self.menu_btn.setAutoExclusive(False)
        self.menu_btn.setObjectName("menu_btn")
        self.horizontalLayout_2.addWidget(self.menu_btn)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.nav_text = QtWidgets.QLabel(self.top_bar)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.nav_text.setFont(font)
        self.nav_text.setStyleSheet("")
        self.nav_text.setObjectName("nav_text")
        self.horizontalLayout_2.addWidget(self.nav_text)
        self.User_L = QtWidgets.QLabel(self.top_bar)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(10)
        self.User_L.setFont(font)
        self.User_L.setObjectName("User_L")
        self.horizontalLayout_2.addWidget(self.User_L)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.RANIL_logo = QtWidgets.QLabel(self.top_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RANIL_logo.sizePolicy().hasHeightForWidth())
        self.RANIL_logo.setSizePolicy(sizePolicy)
        self.RANIL_logo.setMaximumSize(QtCore.QSize(65, 65))
        self.RANIL_logo.setText("")
        self.RANIL_logo.setPixmap(QtGui.QPixmap(":/Icons/images/Ranil_ICON.png"))
        self.RANIL_logo.setScaledContents(True)
        self.RANIL_logo.setObjectName("RANIL_logo")
        self.horizontalLayout_2.addWidget(self.RANIL_logo)
        self.verticalLayout_2.addWidget(self.top_bar)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.scrollArea.setFont(font)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.sideBar = QtWidgets.QWidget()
        self.sideBar.setGeometry(QtCore.QRect(0, 0, 200, 612))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sideBar.sizePolicy().hasHeightForWidth())
        self.sideBar.setSizePolicy(sizePolicy)
        self.sideBar.setMinimumSize(QtCore.QSize(200, 0))
        self.sideBar.setProperty("setVisible", False)
        self.sideBar.setObjectName("sideBar")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.sideBar)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sales_sdbtn = QtWidgets.QPushButton(self.sideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sales_sdbtn.sizePolicy().hasHeightForWidth())
        self.sales_sdbtn.setSizePolicy(sizePolicy)
        self.sales_sdbtn.setMinimumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sales_sdbtn.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/Icons/increasing.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sales_sdbtn.setIcon(icon1)
        self.sales_sdbtn.setIconSize(QtCore.QSize(25, 25))
        self.sales_sdbtn.setCheckable(True)
        self.sales_sdbtn.setAutoExclusive(True)
        self.sales_sdbtn.setObjectName("sales_sdbtn")
        self.verticalLayout.addWidget(self.sales_sdbtn)
        self.transaction_sdbtn = QtWidgets.QPushButton(self.sideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transaction_sdbtn.sizePolicy().hasHeightForWidth())
        self.transaction_sdbtn.setSizePolicy(sizePolicy)
        self.transaction_sdbtn.setMinimumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.transaction_sdbtn.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/Icons/transaction-history.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.transaction_sdbtn.setIcon(icon2)
        self.transaction_sdbtn.setIconSize(QtCore.QSize(25, 25))
        self.transaction_sdbtn.setCheckable(True)
        self.transaction_sdbtn.setAutoExclusive(True)
        self.transaction_sdbtn.setObjectName("transaction_sdbtn")
        self.verticalLayout.addWidget(self.transaction_sdbtn)
        self.inventory_sdbtn = QtWidgets.QPushButton(self.sideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inventory_sdbtn.sizePolicy().hasHeightForWidth())
        self.inventory_sdbtn.setSizePolicy(sizePolicy)
        self.inventory_sdbtn.setMinimumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.inventory_sdbtn.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/Icons/inventory (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.inventory_sdbtn.setIcon(icon3)
        self.inventory_sdbtn.setIconSize(QtCore.QSize(25, 25))
        self.inventory_sdbtn.setCheckable(True)
        self.inventory_sdbtn.setAutoExclusive(True)
        self.inventory_sdbtn.setObjectName("inventory_sdbtn")
        self.verticalLayout.addWidget(self.inventory_sdbtn)
        self.records_sdbtn = QtWidgets.QPushButton(self.sideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.records_sdbtn.sizePolicy().hasHeightForWidth())
        self.records_sdbtn.setSizePolicy(sizePolicy)
        self.records_sdbtn.setMinimumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.records_sdbtn.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icons/Icons/folder (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.records_sdbtn.setIcon(icon4)
        self.records_sdbtn.setIconSize(QtCore.QSize(25, 25))
        self.records_sdbtn.setCheckable(True)
        self.records_sdbtn.setAutoExclusive(True)
        self.records_sdbtn.setObjectName("records_sdbtn")
        self.verticalLayout.addWidget(self.records_sdbtn)
        self.reports_sdbtn = QtWidgets.QPushButton(self.sideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reports_sdbtn.sizePolicy().hasHeightForWidth())
        self.reports_sdbtn.setSizePolicy(sizePolicy)
        self.reports_sdbtn.setMinimumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.reports_sdbtn.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Icons/Icons/report (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reports_sdbtn.setIcon(icon5)
        self.reports_sdbtn.setIconSize(QtCore.QSize(25, 25))
        self.reports_sdbtn.setCheckable(True)
        self.reports_sdbtn.setAutoExclusive(True)
        self.reports_sdbtn.setObjectName("reports_sdbtn")
        self.verticalLayout.addWidget(self.reports_sdbtn)
        self.help_sdbtn = QtWidgets.QPushButton(self.sideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.help_sdbtn.sizePolicy().hasHeightForWidth())
        self.help_sdbtn.setSizePolicy(sizePolicy)
        self.help_sdbtn.setMinimumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.help_sdbtn.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Icons/Icons/information.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help_sdbtn.setIcon(icon6)
        self.help_sdbtn.setIconSize(QtCore.QSize(25, 25))
        self.help_sdbtn.setCheckable(True)
        self.help_sdbtn.setAutoExclusive(True)
        self.help_sdbtn.setObjectName("help_sdbtn")
        self.verticalLayout.addWidget(self.help_sdbtn)
        self.maintenance_sdbtn = QtWidgets.QPushButton(self.sideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maintenance_sdbtn.sizePolicy().hasHeightForWidth())
        self.maintenance_sdbtn.setSizePolicy(sizePolicy)
        self.maintenance_sdbtn.setMinimumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.maintenance_sdbtn.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Icons/Icons/optimizing.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.maintenance_sdbtn.setIcon(icon7)
        self.maintenance_sdbtn.setIconSize(QtCore.QSize(25, 25))
        self.maintenance_sdbtn.setCheckable(True)
        self.maintenance_sdbtn.setAutoExclusive(True)
        self.maintenance_sdbtn.setObjectName("maintenance_sdbtn")
        self.verticalLayout.addWidget(self.maintenance_sdbtn)
        self.about_sdbtn = QtWidgets.QPushButton(self.sideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.about_sdbtn.sizePolicy().hasHeightForWidth())
        self.about_sdbtn.setSizePolicy(sizePolicy)
        self.about_sdbtn.setMinimumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.about_sdbtn.setFont(font)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/Icons/Icons/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.about_sdbtn.setIcon(icon8)
        self.about_sdbtn.setIconSize(QtCore.QSize(25, 25))
        self.about_sdbtn.setCheckable(True)
        self.about_sdbtn.setAutoExclusive(True)
        self.about_sdbtn.setObjectName("about_sdbtn")
        self.verticalLayout.addWidget(self.about_sdbtn)
        self.log_out_sdbtn = QtWidgets.QPushButton(self.sideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log_out_sdbtn.sizePolicy().hasHeightForWidth())
        self.log_out_sdbtn.setSizePolicy(sizePolicy)
        self.log_out_sdbtn.setMinimumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.log_out_sdbtn.setFont(font)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/Icons/Icons/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.log_out_sdbtn.setIcon(icon9)
        self.log_out_sdbtn.setIconSize(QtCore.QSize(25, 25))
        self.log_out_sdbtn.setObjectName("log_out_sdbtn")
        self.verticalLayout.addWidget(self.log_out_sdbtn)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.scrollArea.setWidget(self.sideBar)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_2)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.verticalLayout_2.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nav_text.setText(_translate("MainWindow", "Ranil\'s Poultry Shop"))
        self.User_L.setText(_translate("MainWindow", "TextLabel"))
        self.sales_sdbtn.setText(_translate("MainWindow", "SALES"))
        self.transaction_sdbtn.setText(_translate("MainWindow", "TRANSACTION"))
        self.inventory_sdbtn.setText(_translate("MainWindow", "INVENTORY"))
        self.records_sdbtn.setText(_translate("MainWindow", "RECORDS"))
        self.reports_sdbtn.setText(_translate("MainWindow", "REPORTS"))
        self.help_sdbtn.setText(_translate("MainWindow", "HELP"))
        self.maintenance_sdbtn.setText(_translate("MainWindow", "MAINTENANCE"))
        self.about_sdbtn.setText(_translate("MainWindow", "ABOUT"))
        self.log_out_sdbtn.setText(_translate("MainWindow", "LOGOUT"))
import assets.All_In_Resource_rc
