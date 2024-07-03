import sys
import mysql.connector
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt 
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream
from Database.DBController import dbcont
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image

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
        algo_data = self.db.get_inventory()

        # Create a DataFrame
        df = pd.DataFrame(algo_data, columns=['ReceiptID', 'ProductID', 'Quantity', 'Price', 'Date'])

        # Convert 'Date' to datetime format
        df['Date'] = pd.to_datetime(df['Date'])

        # Add a 'Month' column
        df['Month'] = df['Date'].dt.to_period('M')

        # Calculate monthly sales for each product
        df['SalesValue'] = df['Quantity'] * df['Price']
        monthly_sales = df.groupby(['ProductID', 'Month'])['SalesValue'].sum().reset_index()

        # Perform ABC categorization for each month
        def abc_categorization(monthly_sales):
            categories = []
            for period, group in monthly_sales.groupby('Month'):
                group = group.copy()
                group = group.sort_values('SalesValue', ascending=False)
                group['CumulativeSum'] = group['SalesValue'].cumsum()
                group['CumulativePercentage'] = 100 * group['CumulativeSum'] / group['SalesValue'].sum()
                
                group['Category'] = np.where(group['CumulativePercentage'] <= 80, 'A', 
                                    np.where(group['CumulativePercentage'] <= 95, 'B', 'C'))
                categories.append(group)
            
            categorized_df = pd.concat(categories)
            return categorized_df

        categorized_sales = abc_categorization(monthly_sales)

        # Output the result
        print(categorized_sales)
        return categorized_sales

    # Test method
    def classify_abc(self):
        df_result = self.abc_classification()
        print(df_result)

    #=======================PDF SECTION===========================================#
    def generate_sales_graph(self):
        # Generate data for the graph (example: monthly sales for category A)
        df_classification = self.abc_classification()
        category_a_sales = df_classification[df_classification['Category'] == 'A']
        
        # Group by month and sum sales values
        monthly_sales_data = category_a_sales.groupby('Month')['SalesValue'].sum()

        # Create the plot
        plt.figure(figsize=(10, 6))
        plt.plot(monthly_sales_data.index.astype(str), monthly_sales_data.values, marker='o', linestyle='-', label='Category A Products')
        plt.title('Monthly Sales for Category A Products')
        plt.xlabel('Month')
        plt.ylabel('Sales Value')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.legend()  # Add legend for Category A

        # Save the plot to a BytesIO object
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        
        # Clear the plot
        plt.clf()

        return buffer

    def print_to_pdf(self):
    # Create a document
        pdf_filename = "Inventory_Report.pdf"
        pdf = SimpleDocTemplate(pdf_filename, pagesize=letter)
        
        # Define styles
        styles = getSampleStyleSheet()
        elements = []
        
        # Add title and date
        title = Paragraph("Ranil's Inventory Report", styles['Title'])
        date = Paragraph("For the date: " + self.FDate_DE.date().toString("yyyy-MM-dd"), styles['Normal'])
        
        elements.append(title)
        elements.append(Spacer(1, 12))
        # Add address
        address_text = "6, Rizal Avenue, Balite, Montalban (Rodriguez) Rizal"
        address = Paragraph(address_text, styles['Title'])
        elements.append(address)
        elements.append(Spacer(1, 24))
        elements.append(date)
        elements.append(Spacer(1, 12))  # Reduce spacer for a bit tighter layout
        
        
        
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

        class_a = df_classification[df_classification['Category'] == 'A']
        class_b = df_classification[df_classification['Category'] == 'B']
        class_c = df_classification[df_classification['Category'] == 'C']

        elements.append(Paragraph(f"Class A products: {', '.join(class_a['ProductID'].astype(str).tolist())}", styles['Normal']))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(f"Class B products: {', '.join(class_b['ProductID'].astype(str).tolist())}", styles['Normal']))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(f"Class C products: {', '.join(class_c['ProductID'].astype(str).tolist())}", styles['Normal']))
        
        # Add space
        elements.append(Spacer(1, 24))

        # Generate sales graph
        sales_graph_buffer = self.generate_sales_graph()

        # Add the graph to the PDF
        sales_graph_image = Image(sales_graph_buffer)
        sales_graph_image.drawWidth = 500
        sales_graph_image.drawHeight = 300
        elements.append(Paragraph("Monthly Sales for Category A Products:", styles['Heading2']))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph("Graph showing monthly sales for Category A products:", styles['Normal']))
        elements.append(Spacer(1, 12))
        elements.append(sales_graph_image)
        
        # Build PDF
        generated_info = f"Report Generated on: {datetime.today().strftime('%Y-%m-%d %H:%M:%S')}\nReport Generated by: Rheiniel Damasco"  # Replace with actual name
        generated_info_para = Paragraph(generated_info, styles['Normal'])
        elements.append(Spacer(1, 24))
        elements.append(generated_info_para)

        pdf.build(elements)
        print(f"PDF saved as '{pdf_filename}'")
