import sys
import mysql.connector
import pandas as pd
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream
from Database.DBController import dbcont
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

from .Inventory_Report_ui import Ui_MainWindow
from Database.DBController import dbcont
from PyQt5 import QtWidgets, QtGui, QtCore
class Inventory_Report_Window(QMainWindow, Ui_MainWindow):
    db = dbcont()
    
    def __init__(self):
        super(Inventory_Report_Window, self).__init__()
        self.setupUi(self)
        self.set_tableElements()
        self.generateBtn.clicked.connect(self.print_to_pdf)
        self.Search_btn.clicked.connect(self.search)
        self.Refresh_btn.clicked.connect(self.set_tableElements)
        self.pushButton_2.clicked.connect(self.abc_classification)
        

    def set_tableElements(self):
        searchResult = self.db.get_inventory()
        self.tableWidget.setRowCount(0)
        if searchResult:
            self.tableWidget.setRowCount(len(searchResult))
            print(len(searchResult))
            print(searchResult)
            for row_number, row_data in enumerate(searchResult):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))


    def search(self):
        start_date = self.FDate_DE.date().toPyDate()
        end_date = self.TDate_DE.date().toPyDate()
        print(start_date)
        print(end_date)

        if self.radioButton.isChecked() and start_date != end_date:
            searchResult = self.db.search_inventory_rec(start_date, end_date)
        else:
            searchResult = self.db.search_inventory_rec(start_date)

        self.tableWidget.setRowCount(0)
        if searchResult:
            self.tableWidget.setRowCount(len(searchResult))
            print(len(searchResult))
            print(searchResult)
            for row_number, row_data in enumerate(searchResult):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    print('Setting item...')
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        else:
            print('No transactions found for the selected date or date range.')
        
    def pdf_layout_grid(self, pdf):
        pdf.drawString(90, 810, 'x100')
        pdf.drawString(190, 810, 'x200')
        pdf.drawString(290, 810, 'x300')
        pdf.drawString(390, 810, 'x400')
        pdf.drawString(490, 810, 'x500')

        pdf.drawString(10, 100, 'y100')
        pdf.drawString(10, 200, 'y200')
        pdf.drawString(10, 300, 'y300')
        pdf.drawString(10, 400, 'y400')
        pdf.drawString(10, 500, 'y500')
        pdf.drawString(10, 600, 'y600')
        pdf.drawString(10, 700, 'y700')
        pdf.drawString(10, 800, 'y800')
#====================================ALGO SECTION===========================================# 
    def abc_classification(self):
        algo_data = self.db.get_algo_data()

        # Create a DataFrame
        df = pd.DataFrame(algo_data, columns=['ProductID', 'ProductName', 'MonthlyDemand', 'UnitPrice'])

        # Calculate the total monthly revenue for each product
        df = self.calculate_monthly_consumption(df)

        # Sort products by total monthly revenue in descending order
        df = self.sort_prods(df)

        # Calculate cumulative percentage of total revenue and categorize items
        df = self.categorize_items(df)

        print(df)
        return df

    def calculate_monthly_consumption(self, df):
        df['monthly_consumption_value'] = df['UnitPrice'] * df['MonthlyDemand']
        return df

    def sort_prods(self, df):
        df = df.sort_values(by='monthly_consumption_value', ascending=False)
        return df

    def categorize_items(self, df):
        total_value = df['monthly_consumption_value'].sum()
        df['cumulative_percentage'] = df['monthly_consumption_value'].cumsum() / total_value * 100

        def categorize(row):
            if row['cumulative_percentage'] <= 70:
                return 'A'
            elif row['cumulative_percentage'] <= 90:
                return 'B'
            else:
                return 'C'

        df['category'] = df.apply(categorize, axis=1)
        return df
    
    #Test method
    def classify_abc(self):
        df_result = self.abc_classification
        print(df_result)
#=======================PDF SECTION===========================================#
    def print_to_pdf(self):
        # Create a document
        pdf_filename = "Inventory_Report.pdf"
        pdf = SimpleDocTemplate(pdf_filename, pagesize=letter)
        
        # Define styles
        styles = getSampleStyleSheet()
        elements = []
        
        # Add title and date
        title = Paragraph("Inventory Report", styles['Title'])
        date = Paragraph("For the date: " + self.FDate_DE.date().toString("yyyy-MM-dd"), styles['Normal'])
        elements.append(title)
        elements.append(Spacer(1, 12))
        elements.append(date)
        elements.append(Spacer(1, 24))
        
        # Add space
        elements.append(Paragraph("<br/>", styles['Normal']))

        # Table data
        data = []

        # Add table headers
        headers = []
        for column in range(self.tableWidget.columnCount()):
            header_item = self.tableWidget.horizontalHeaderItem(column)
            if header_item is not None:
                headers.append(header_item.text())
            else:
                headers.append('')
        data.append(headers)
        
        # Add table rows
        for row in range(self.tableWidget.rowCount()):
            row_data = []
            for column in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, column)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append('')
            data.append(row_data)
        
        # Create table
        table = Table(data)
        
        # Table style
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        
        # Add table to elements
        elements.append(table)

        # Add ABC classification results
        df_classification = self.abc_classification()
        elements.append(Spacer(1, 24))
        elements.append(Paragraph("ABC Classification:", styles['Heading2']))
        elements.append(Spacer(1, 12))

        class_a = df_classification[df_classification['category'] == 'A']
        class_b = df_classification[df_classification['category'] == 'B']
        class_c = df_classification[df_classification['category'] == 'C']

        elements.append(Paragraph(f"Class A products: {', '.join(class_a['ProductName'].tolist())}", styles['Normal']))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(f"Class B products: {', '.join(class_b['ProductName'].tolist())}", styles['Normal']))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(f"Class C products: {', '.join(class_c['ProductName'].tolist())}", styles['Normal']))
        
        # Build PDF
        pdf.build(elements)
        print(f"PDF saved as '{pdf_filename}'")
