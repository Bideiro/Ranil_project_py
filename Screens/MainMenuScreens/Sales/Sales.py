import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget, QTableWidgetItem,  QTableWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream
from Database.DBController import dbcont
from .Sales_ui import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
class Sales_Window(QMainWindow, Ui_MainWindow):
    
    db = dbcont()
    
    def __init__(self):
        super(Sales_Window,self).__init__()
        self.setupUi(self)

        self.Sales_Table.setColumnWidth(0,200)
        self.Sales_Table.setColumnWidth(1,200)
        self.Sales_Table.setColumnWidth(2,150)
        self.Sales_Table.setColumnWidth(3,150)
        self.Sales_Table.setColumnWidth(4,150)
        self.Sales_Table.setColumnWidth(5,250)
        self.Sales_Table.setColumnWidth(6,200)
        self.set_tableElements()
        
        self.Refresh_btn.clicked.connect(self.set_tableElements)
        self.Search_btn.clicked.connect(self.search)
        self.annualSalesbtn.clicked.connect(self.changeTableYearly)
        self.dailySalesbtn.clicked.connect(self.set_tableElements)
        self.monthlySalesbtn.clicked.connect(self.changeTableMonthly)
        #self.Sales_Table.itemClicked.connect(self.clicked_item)
        self.comboBox.setVisible(False)
        
        
    def set_tableElements(self):
        result = self.db.get_all_sales()
        self.search_LE.clear()
        self.Sales_Table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.Sales_Table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                if column_number == 6 :
                    data = self.db.get_payment_type(id= data)
                if column_number == 0:
                    data = data.strftime('%B %d, %Y %H:%M')
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignCenter)
                self.Sales_Table.setItem(row_number, column_number, item)
        
    def search(self):
        searchResult = self.db.search_sales(self.search_LE.text())
        self.search_LE.clear()
        self.Sales_Table.setRowCount(0)
        if searchResult:
            for row_number, row_data in enumerate(searchResult):
                self.Sales_Table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if column_number == 6 :
                        data = self.db.get_payment_type(id= data)
                    if column_number == 0:
                        data = data.strftime('%B %d, %Y %H:%M')
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.Sales_Table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
    def changeTableYearly(self):
        result = self.db.set_yearly_sales() #Shows monthly sales in wrong column
        self.Sales_Table.setRowCount(len(result))
        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):
                if column_number == 6:
                    data = self.db.get_id_value(id= data, unit= True)
                if column_number == 7:
                    data = self.db.get_id_value(id= data, cate= True)
                self.Sales_Table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        added_years = set()  # Set to track added years
        for row_data in result:
            year = row_data[0]  # Extract the year from the first column of the row_data
        if year not in added_years:
            self.comboBox.addItem(str(year))  # Ensure year is a string before adding
            added_years.add(year)
        self.Sales_Table.setColumnHidden(2, True)  # Hide the third column (index 2)
        self.Sales_Table.setColumnHidden(3, True)  # Hide the fourth column (index 3)
        self.Sales_Table.setHorizontalHeaderLabels(['Year', 'Total', '', ''])

    def changeTableMonthly(self):
                #==========================================COMBO BOX CONFIG==============================#
                self.comboBox.setVisible(True)
                years = self.db.get_years()  # Assuming self.db.get_years() returns a list of tuples like [(2011,), (2012,), ...]
                years_formatted = []

                existing_years = set(self.comboBox.itemText(i) for i in range(self.comboBox.count()))  # Get existing years

                for year_tuple in years:
                    if len(year_tuple) >= 2:  # Check if the tuple has at least two elements
                        year_str = f"{year_tuple[0]} - {year_tuple[1]}"
                    elif len(year_tuple) == 1:  # Handle tuples with only one element
                        year_str = f"{year_tuple[0]}"  # Append the single element directly
                    else:
                        # Handle the case where the tuple is empty or unexpected format
                        print(f"Warning: Invalid tuple format: {year_tuple}")
                        continue  # Skip this invalid tuple

                    if year_str not in existing_years:  # Check if the year is already in the comboBox
                        years_formatted.append(year_str)
                        existing_years.add(year_str)

                self.comboBox.addItems(years_formatted)
                #=======================================================================================#
                curryear = self.comboBox.currentText()
                sql= f"""
                    SELECT 
                        MONTH(PurchaseDate) AS Month,
                        SUM(Price) AS TotalSum
                    FROM 
                        transaction_receipts
                    WHERE
                        YEAR(PurchaseDate) = '{curryear}'
                    GROUP BY 
                        MONTH(PurchaseDate)
                    ORDER BY 
                        Month;
                    """
                self.db.mycursor.execute(sql)
                result= self.db.mycursor.fetchall()
                self.Sales_Table.setRowCount(len(result))
                for row_number, row_data in enumerate(result):
                    for column_number, data in enumerate(row_data):
                        if column_number == 6:
                            data = self.db.get_id_value(id=data, unit=True)
                        if column_number == 7:
                            data = self.db.get_id_value(id=data, cate=True)
                        item = QTableWidgetItem(str(data))
                        self.Sales_Table.setItem(row_number, column_number, item)
                self.Sales_Table.setColumnHidden(2, True)  # Hide the third column (index 2)
                self.Sales_Table.setColumnHidden(3, True)  # Hide the fourth column (index 3)
                self.Sales_Table.setHorizontalHeaderLabels(['Month', 'Total', '', ''])