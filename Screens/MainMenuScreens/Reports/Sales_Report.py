
import datetime
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

from reportlab.lib.pagesizes import letter

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

from .Sales_Report_ui import Ui_MainWindow
from Database.DBController import dbcont
from PyQt5 import QtWidgets, QtGui, QtCore
class Sales_Report_Window(QMainWindow, Ui_MainWindow):

    back_btnsgl = QtCore.pyqtSignal()
    
    db = dbcont()
    def __init__(self):
        super(Sales_Report_Window, self).__init__()
        self.setupUi(self)
        self.set_tableElements()
        self.generateBtn.clicked.connect(self.print_to_pdf)
        self.Search_btn.clicked.connect(self.search)
        self.Refresh_btn.clicked.connect(self.set_tableElements)
        self.backBtn.clicked.connect(lambda: self.back_btnsgl.emit())
        
    def search(self):
        start_date = self.SDate_DE.date().toPyDate()
        end_date = self.EDate_DE.date().toPyDate()
        
        if self.DRange_RB.isChecked() and start_date != end_date:
            searchResult = self.db.search_sales_rep(start_date, end_date)
        else:
            searchResult = self.db.search_sales_rep(start_date)

        self.tableWidget.setRowCount(0)
        if searchResult:
            for row_number, row_data in enumerate(searchResult):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if column_number == 0:
                        data = data.strftime('%B %d, %Y %H:%M')
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        else:
            print('No transactions found for the selected date or date range.')

    def set_tableElements(self):
        self.set_daily_tableElements()
        self.set_monthly_tableElements()
        self.set_yearly_tableElements()
        
    def set_daily_tableElements(self):
        Result = self.db.get_sales_report(daily= True)
        self.Daily_table.setRowCount(0)
        if Result:
            for row_number, row_data in enumerate(Result):
                self.Daily_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    # if column_number == 0:
                    #     data = data.strftime('%B %d, %Y')
                    self.Daily_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                    
    def set_monthly_tableElements(self):
        Result = self.db.get_sales_report(monthly=True)
        self.Monthly_table.setRowCount(0)
        if Result:
            for row_number, row_data in enumerate(Result):
                self.Monthly_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if column_number == 0:
                        date_time = datetime.datetime(1900, data, 1)
                        data = date_time.strftime('%B')
                    self.Monthly_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                    
    def set_yearly_tableElements(self):
        Result = self.db.get_sales_report(yearly=True)
        self.Yearly_table.setRowCount(0)
        if Result:
            for row_number, row_data in enumerate(Result):
                self.Yearly_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.Yearly_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    
    def print_to_pdf(self):
        # Create a document
        pdf_filename = "Sales_Report.pdf"
        pdf = SimpleDocTemplate(pdf_filename, pagesize=letter)
        
        # Define styles
        styles = getSampleStyleSheet()
        elements = []
        
        # Add title and date
        title = Paragraph("Ranil's Sales Report", styles['Title'])
        date = Paragraph("For the date:  " + self.SDate_DE.date().toString("yyyy-MM-dd"), styles['Normal'])
        elements.append(title)
        elements.append(Spacer(1, 12))
        # Add address
        address_text = "6, Rizal Avenue, Balite, Montalban (Rodriguez) Rizal"
        address = Paragraph(address_text, styles['Title'])
        elements.append(address)
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
        generated_info = f"Report Generated on: {datetime.today().strftime('%Y-%m-%d %H:%M:%S')}\nReport Generated by: Rheiniel Damasco"  # Replace with actual name
        generated_info_para = Paragraph(generated_info, styles['Normal'])
        elements.append(Spacer(1, 24))
        elements.append(generated_info_para)

        pdf.build(elements)
        print(f"PDF saved as '{pdf_filename}'")

