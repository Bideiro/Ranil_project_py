# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\dei\Documents\Programming\Ranil_projecy_py\Screens\MainMenuScreens\Transaction\Transaction_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#Lchick_btn{\n"
"background-color: #F9A518;\n"
"}\n"
"#dog_btn{\n"
"background-color: #096033;\n"
"color: white\n"
"}\n"
"#fert_btn{\n"
"background-color: #F9A518;\n"
"}\n"
"#feeds_btn{\n"
"background-color: black;\n"
"color: white\n"
"}\n"
"#med_btn{\n"
"background-color: #C69570;\n"
"color: white\n"
"}\n"
"#cat_btn{\n"
"background-color: #ABE27D;\n"
"}\n"
"#petess_btn{\n"
"background-color: #A02F24;\n"
"color: white\n"
"}\n"
"#others_btn{\n"
"background-color: #C0C0C0;\n"
"}\n"
".QLineEdit{\n"
"border : 2px solid #C0C0C0;\n"
"background-color:rgba(0,0,0,0);\n"
"color: #096033 \n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("#pushButton{\n"
"background-color: #F9A518;\n"
"}\n"
"#pushButton_2{\n"
"background-color: #096033;\n"
"color: white\n"
"}\n"
"#pushButton_3{\n"
"background-color: #F9A518;\n"
"}\n"
"#pushButton_4{\n"
"background-color: black;\n"
"color: white\n"
"}\n"
"#pushButton_5{\n"
"background-color: #C69570;\n"
"color: white\n"
"}\n"
"#pushButton_7{\n"
"background-color: #ABE27D;\n"
"}\n"
"#pushButton_8{\n"
"background-color: #A02F24;\n"
"color: white\n"
"}\n"
"#pushButton_9{\n"
"background-color: #C0C0C0;\n"
"}\n"
".QLineEdit{\n"
"border : 2px solid #C0C0C0;\n"
"background-color:rgba(0,0,0,0);\n"
"color: #096033 \n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_4.addWidget(self.lineEdit)
        self.verticalLayout_5.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget_6)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.dog_btn = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dog_btn.sizePolicy().hasHeightForWidth())
        self.dog_btn.setSizePolicy(sizePolicy)
        self.dog_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.dog_btn.setObjectName("dog_btn")
        self.verticalLayout_3.addWidget(self.dog_btn)
        self.fert_btn = QtWidgets.QPushButton(self.widget_2)
        self.fert_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.fert_btn.setObjectName("fert_btn")
        self.verticalLayout_3.addWidget(self.fert_btn)
        self.Lchick_btn = QtWidgets.QPushButton(self.widget_2)
        self.Lchick_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.Lchick_btn.setObjectName("Lchick_btn")
        self.verticalLayout_3.addWidget(self.Lchick_btn)
        self.horizontalLayout.addWidget(self.widget_2)
        self.widget_4 = QtWidgets.QWidget(self.widget_6)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cat_btn = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cat_btn.sizePolicy().hasHeightForWidth())
        self.cat_btn.setSizePolicy(sizePolicy)
        self.cat_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.cat_btn.setObjectName("cat_btn")
        self.verticalLayout_2.addWidget(self.cat_btn)
        self.petess_btn = QtWidgets.QPushButton(self.widget_4)
        self.petess_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.petess_btn.setObjectName("petess_btn")
        self.verticalLayout_2.addWidget(self.petess_btn)
        self.others_btn = QtWidgets.QPushButton(self.widget_4)
        self.others_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.others_btn.setObjectName("others_btn")
        self.verticalLayout_2.addWidget(self.others_btn)
        self.horizontalLayout.addWidget(self.widget_4)
        self.widget_3 = QtWidgets.QWidget(self.widget_6)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.feeds_btn = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feeds_btn.sizePolicy().hasHeightForWidth())
        self.feeds_btn.setSizePolicy(sizePolicy)
        self.feeds_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.feeds_btn.setObjectName("feeds_btn")
        self.verticalLayout.addWidget(self.feeds_btn)
        self.med_btn = QtWidgets.QPushButton(self.widget_3)
        self.med_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.med_btn.setObjectName("med_btn")
        self.verticalLayout.addWidget(self.med_btn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.widget_3)
        self.verticalLayout_5.addWidget(self.widget_6)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_2.addWidget(self.widget)
        spacerItem3 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setText(_translate("MainWindow", "Search"))
        self.dog_btn.setText(_translate("MainWindow", "DOG FOOD"))
        self.fert_btn.setText(_translate("MainWindow", "FERTILIZERS"))
        self.Lchick_btn.setText(_translate("MainWindow", "LIVE CHICK"))
        self.cat_btn.setText(_translate("MainWindow", "CAT FOOD"))
        self.petess_btn.setText(_translate("MainWindow", "PET ESSENTIALS"))
        self.others_btn.setText(_translate("MainWindow", "OTHERS"))
        self.feeds_btn.setText(_translate("MainWindow", "FEEDS"))
        self.med_btn.setText(_translate("MainWindow", "MEDICINE"))
