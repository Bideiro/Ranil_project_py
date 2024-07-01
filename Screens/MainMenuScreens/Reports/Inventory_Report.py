import sys
import mysql.connector
import pandas as pd
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

from .Inventory_Report_ui import Ui_MainWindow
from Database.DBController import dbcont
from PyQt5 import QtWidgets, QtGui, QtCore
class Inventory_Report_Window(QMainWindow, Ui_MainWindow):

    
    def __init__(self):
        super(Inventory_Report_Window, self).__init__()
        self.setupUi(self)
        self.db = dbcont('admin', 123456)
        self.set_tableElements()
        self.generateBtn.clicked.connect(self.print_to_pdf)
        self.Search_btn.clicked.connect(self.search)
        self.radioButton.toggled.connect(self.dateRangeToggle)
        self.dateEdit.setCalendarPopup(True)

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
    
    def dateRangeToggle(self, selected):
        if selected:
            self.dateEdit2.setEnabled(True)
        else:
            self.dateEdit2.setEnabled(False)
    
    def get_date_1(self):
        selected_date_1 = self.dateEdit.date()
        date_str = selected_date_1.toString('yyyy-MM-dd')
        print(f"Selected Date: {date_str}")
        return date_str

    def get_date_2(self):
        selected_date_2 = self.dateEdit2.date()
        date_str2 = selected_date_2.toString('yyyy-MM-dd')
        print(f"End Date:  {date_str2}")
        return date_str2

    def search(self):
        date = self.dateEdit.date().toPyDate()

        searchResult = self.db.search_inventory_rec(date)
        self.tableWidget.setRowCount(0)
        if searchResult:
            self.tableWidget.setRowCount(len(searchResult))
            print(len(searchResult))
            print(searchResult)
            for row_number, row_data in enumerate(searchResult):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    # if column_number == 6:
                    #     data = self.db.get_id_value(id= data, unit= True)
                    # if column_number == 7:
                    #     data = self.db.get_id_value(id= data, cate= True)
                    print('Setting item...')
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        else:
            print('No transactions found for the selected date.')
        
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
    
    def abc_classification(self):
        # Define the products and their data
        products = {
            'Product': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
            'Monthly Demand': [450, 187, 328, 59, 178, 211, 69],
            'Unit Price': [30, 280, 120, 370, 200, 120, 220]
        }

        # Create a DataFrame
        df = pd.DataFrame(products)

        # Calculate the total monthly revenue for each product
        df['Monthly Revenue'] = df['Monthly Demand'] * df['Unit Price']

        # Sort products by total monthly revenue in descending order
        df = df.sort_values(by='Monthly Revenue', ascending=False)

        # Calculate cumulative percentage of total revenue
        df['Cumulative Revenue'] = df['Monthly Revenue'].cumsum()
        df['Cumulative Percentage'] = df['Cumulative Revenue'] / df['Monthly Revenue'].sum() * 100

        # Classify products into A, B, C categories
        total_products = len(df)
        class_a_cutoff = int(total_products * 0.2)  # 20% of products
        class_b_cutoff = int(total_products * 0.5)  # Next 30% of products

        def classify(row, index):
            if index < class_a_cutoff:
                return 'A'
            elif index < class_b_cutoff:
                return 'B'
            else:
                return 'C'

        df['Class'] = [classify(row, idx) for idx, row in df.iterrows()]

        # Output the classification
        print(df[['Product', 'Monthly Demand', 'Unit Price', 'Monthly Revenue', 'Cumulative Percentage', 'Class']])

        # Display results as Class A, B, C
        class_a = df[df['Class'] == 'A']['Product'].tolist()
        class_b = df[df['Class'] == 'B']['Product'].tolist()
        class_c = df[df['Class'] == 'C']['Product'].tolist()

        return class_a, class_b, class_c

    def print_to_pdf(self):
        # Create a document
        pdf_filename = "Inventory_Report.pdf"
        pdf = SimpleDocTemplate(pdf_filename, pagesize=letter)
        
        # Define styles
        styles = getSampleStyleSheet()
        elements = []
        
        # Add title and date
        title = Paragraph("Ranil's Inventory Report", styles['Title'])
        date = Paragraph("For the date:  " + self.dateEdit.date().toString("yyyy-MM-dd"), styles['Normal'])
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
        class_a, class_b, class_c = self.abc_classification()
        elements.append(Spacer(1, 24))
        elements.append(Paragraph("ABC Classification:", styles['Heading2']))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(f"Class A products: {', '.join(class_a)}", styles['Normal']))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(f"Class B products: {', '.join(class_b)}", styles['Normal']))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(f"Class C products: {', '.join(class_c)}", styles['Normal']))
        
        # Build PDF
        pdf.build(elements)
        print(f"PDF saved as '{pdf_filename}'")

