import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QTableWidgetItem
from PyQt5.QtCore import Qt

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from datetime import datetime

from PyQt5.QtGui import QPalette, QColor
from .User_Logs_ui import Ui_MainWindow
from Database.DBController import dbcont
from Database.DBController import UserMana
class User_Logs_Window(QMainWindow, Ui_MainWindow):
    
    db = dbcont()
    User = UserMana()
    
    def __init__(self):
        super(User_Logs_Window,self).__init__()
        self.setupUi(self)
        self.set_tableElements()
        
        palette = self.Log_Table.palette()
        palette.setColor(QPalette.AlternateBase, QColor(238, 234, 224))
        self.Log_Table.setPalette(palette)
        
        self.Log_Table.setColumnWidth(0,150)
        self.Log_Table.setColumnWidth(1,150)
        self.Log_Table.setColumnWidth(2,150)
        self.Log_Table.setColumnWidth(3,150)
        self.Log_Table.setColumnWidth(4,200)

        self.reportBtn.clicked.connect(self.print_to_pdf)
        
        
    def set_tableElements(self):
            self.Log_Table.setRowCount(0)
            result = []
            result = self.db.get_logs()
            self.Log_Table.setRowCount(len(result))
            for row_number, row_data in enumerate(result):
                for column_number, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.Log_Table.setItem(row_number, column_number, item)

    def print_to_pdf(self):
    # Create a document
        pdf_filename = "User_Logs_Report.pdf"
        pdf = SimpleDocTemplate(pdf_filename, pagesize=letter)
        
        # Define styles
        styles = getSampleStyleSheet()
        elements = []
        now = datetime.now()
        
        # Add title and date
        title = Paragraph("Ranil's Inventory Report", styles['Title'])
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        date = Paragraph("For the date: " + dt_string, styles['Normal'])
        
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
        for column in range(self.Log_Table.columnCount()):
            header_item = self.Log_Table.horizontalHeaderItem(column)
            if header_item is not None:
                headers.append(header_item.text())
            else:
                headers.append('')
        data.append(headers)
        
        # Add table rows
        for row in range(self.Log_Table.rowCount()):
            row_data = []
            for column in range(self.Log_Table.columnCount()):
                item = self.Log_Table.item(row, column)
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
        generated_info = f"Report Generated on: {datetime.today().strftime('%Y-%m-%d %H:%M:%S')}\nReport Generated by: " + self.User.WName  
        generated_info_para = Paragraph(generated_info, styles['Normal'])
        elements.append(Spacer(1, 24))
        elements.append(generated_info_para)

        pdf.build(elements)
        print(f"PDF saved as '{pdf_filename}'")
