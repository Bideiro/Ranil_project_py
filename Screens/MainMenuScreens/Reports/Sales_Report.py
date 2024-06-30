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

from .Sales_Report_ui import Ui_MainWindow
from Database.DBController import dbcont
from PyQt5 import QtWidgets, QtGui, QtCore
class Sales_Report_Window(QMainWindow, Ui_MainWindow):

    
    def __init__(self):
        super(Sales_Report_Window, self).__init__()
        self.setupUi(self)
        self.db = dbcont('admin', 123456)
        self.set_tableElements()
        self.generateBtn.clicked.connect(self.print_to_pdf)
        self.Search_btn.clicked.connect(self.search)
        self.radioButton.toggled.connect(self.dateRangeToggle)
        self.dateEdit.setCalendarPopup(True)

    def set_tableElements(self):
        self.tableWidget.setRowCount(0)
        searchResult = self.db.get_salesR()
        self.tableWidget.setRowCount(len(searchResult))
        
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

    def search(self):
        date = self.dateEdit.date().toPyDate()

        searchResult = self.db.search_sales_rep(date)
        self.tableWidget.setRowCount(0)
        if searchResult:
            self.tableWidget.setRowCount(len(searchResult))
            #print(len(searchResult))
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

    def print_to_pdf(self):
        # Create a document
        pdf_filename = "Sales_Report.pdf"
        pdf = SimpleDocTemplate(pdf_filename, pagesize=letter)
        
        # Define styles
        styles = getSampleStyleSheet()
        elements = []
        
        # Add title and date
        title = Paragraph("Ranil's Sales Report", styles['Title'])
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

        # Build PDF
        pdf.build(elements)
        print(f"PDF saved as '{pdf_filename}'")

