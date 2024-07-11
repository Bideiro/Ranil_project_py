
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image


from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

from Dialogs.DLog_Alert import DLG_Alert

from .Inventory_Report_ui import Ui_MainWindow
from Database.DBController import dbcont

class Inventory_Report_Window(QMainWindow, Ui_MainWindow):
    db = dbcont()
    
    back_btnsgl = QtCore.pyqtSignal()
    
    def __init__(self):
        super(Inventory_Report_Window, self).__init__()
        self.setupUi(self)
        
        self.tableWidget.setColumnWidth(0,200)
        self.tableWidget.setColumnWidth(1,200)
        self.tableWidget.setColumnWidth(2,150)
        self.tableWidget.setColumnWidth(3,150)
        self.tableWidget.setColumnWidth(4,150)
        
        self.set_tableElements()
        self.generateBtn.clicked.connect(self.print_to_pdf)
        self.Search_btn.clicked.connect(self.search)
        self.Refresh_btn.clicked.connect(self.set_tableElements)
        self.Back_btn.clicked.connect(lambda: self.back_btnsgl.emit())
        

    def set_tableElements(self):
        searchResult = self.db.get_inventory()
        self.tableWidget.setRowCount(0)
        if searchResult:
            for row_number, row_data in enumerate(searchResult):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if column_number == 4:
                        data = data.strftime('%B %d, %Y')
                        
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.tableWidget.setItem(row_number, column_number, item)


    def search(self):
        start_date = self.FDate_DE.date().toPyDate()
        end_date = self.TDate_DE.date().toPyDate()

        if self.radioButton.isChecked() :
            if start_date <= end_date:
                searchResult = self.db.search_inventory_rec(start_date, end_date)
                self.tableWidget.setRowCount(0)
                if searchResult:
                    for row_number, row_data in enumerate(searchResult):
                        self.tableWidget.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            if column_number == 4:
                                data = data.strftime('%B %d, %Y')
                            
                            item = QTableWidgetItem(str(data))
                            item.setTextAlignment(Qt.AlignCenter)
                            self.tableWidget.setItem(row_number, column_number, item)
                else:
                    print('No transactions found for the selected date or date range.')
            else:
                Dlg = DLG_Alert(msg= 'Invalid Date ranges!')
                Dlg.exec()
        else:
            searchResult = self.db.search_inventory_rec(start_date)
            self.tableWidget.setRowCount(0)
            if searchResult:
                for row_number, row_data in enumerate(searchResult):
                    self.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        if column_number == 4:
                            
                            data = data.strftime('%B %d, %Y')
                        item = QTableWidgetItem(str(data))
                        item.setTextAlignment(Qt.AlignCenter)
                        self.tableWidget.setItem(row_number, column_number, item)
            else:
                print('No transactions found for the selected date or date range.')

       
        

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
        
        # Aggregate sales by ProductID and Month
        monthly_sales = df.groupby(['ProductID', 'Month'])['SalesValue'].sum().reset_index()

        # Perform ABC categorization for each month
        def abc_categorization(monthly_sales):
            categories = []
            abc_result = {}

            for period, group in monthly_sales.groupby('Month'):
                group = group.copy()
                group = group.sort_values('SalesValue', ascending=False)

                # Calculate cumulative sum and percentage for the entire group
                group['CumulativeSum'] = group['SalesValue'].cumsum()
                group['CumulativePercentage'] = 100 * group['CumulativeSum'] / group['SalesValue'].sum()

                # Initialize Category column with default value 'C'
                group['Category'] = 'C'

                # Classify Category A
                group.loc[group['CumulativePercentage'] <= 80, 'Category'] = 'A'

                # Classify Category B for remaining items
                group.loc[(group['CumulativePercentage'] > 80) & (group['CumulativePercentage'] <= 95), 'Category'] = 'B'

                # Append the categorized group to the list
                categories.append(group)

                # Store the ABC classification result for the current month
                abc_result[period] = {
                    'A': group[group['Category'] == 'A']['ProductID'].tolist(),
                    'B': group[group['Category'] == 'B']['ProductID'].tolist(),
                    'C': group[group['Category'] == 'C']['ProductID'].tolist(),
                }

            categorized_df = pd.concat(categories)
            return categorized_df, abc_result

        categorized_sales, abc_result = abc_categorization(monthly_sales)

        # Output the result by month and category
        for month, group in categorized_sales.groupby('Month'):
            print(f"{month}:")
            for category in ['A', 'B', 'C']:
                products = group[group['Category'] == category]['ProductID'].tolist()
                print(f"Class {category} Products: {', '.join(map(str, products))}")
            print()

        return categorized_sales, abc_result

#=======================PDF SECTION===========================================#
    def generate_sales_graph(self):
        # Generate data for the graph (example: monthly sales for category A)
        df_classification, _ = self.abc_classification()
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
            
        title_style = ParagraphStyle(
            'TitleStyle',
            parent=styles['Title'],
            fontName='Helvetica-Bold',
            fontSize=14,
            alignment=1,  # Center alignment
            spaceAfter=6,
        )
        normal_centered_style = ParagraphStyle(
            'NormalCentered',
            parent=styles['Normal'],
            fontName='Helvetica',
            fontSize=10,
            alignment=1,  # Center alignment
            spaceAfter=6,
        )
        elements = []
        
        title = Paragraph("Ranil's Poultry Supply", title_style)
        address = Paragraph("6, Rizal Avenue, Balite, Montalban (Rodriguez) Rizal", normal_centered_style)
        cellphone_number = Paragraph("Cellphone Number: (+63)0951 297 4169", normal_centered_style)
        
        # Add title and date
        report_title = Paragraph("Inventory Report", title_style)
        date = Paragraph("For the date: " + self.FDate_DE.date().toString("yyyy-MM-dd"), normal_centered_style)

        elements.append(title)
        elements.append(Spacer(0, 1))
        elements.append(address)
        elements.append(Spacer(1, 1))
        elements.append(cellphone_number)
        elements.append(Spacer(1, 1))
        elements.append(report_title)
        elements.append(Spacer(1, 7))
        elements.append(date)
        elements.append(Spacer(1, 12))  
        
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
        df_classification, abc_result = self.abc_classification()
        elements.append(Spacer(1, 24))
        elements.append(Paragraph("ABC Classification:", styles['Heading2']))
        elements.append(Spacer(1, 12))

        for month, classes in abc_result.items():
            elements.append(Paragraph(f"{month}:", styles['Heading3']))
            elements.append(Spacer(1, 6))
            elements.append(Paragraph(f"Class A products: {', '.join(map(str, classes['A']))}", styles['Normal']))
            elements.append(Spacer(1, 6))
            elements.append(Paragraph(f"Class B products: {', '.join(map(str, classes['B']))}", styles['Normal']))
            elements.append(Spacer(1, 6))
            elements.append(Paragraph(f"Class C products: {', '.join(map(str, classes['C']))}", styles['Normal']))
            elements.append(Spacer(1, 12))
        
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
        
        # Generate and add the new sales graph with product labels
        product_sales_graph_buffer = self.generate_product_sales_graph(df_classification)

        product_sales_graph_image = Image(product_sales_graph_buffer)
        product_sales_graph_image.drawWidth = 500
        product_sales_graph_image.drawHeight = 300
        elements.append(Spacer(1, 24))
        elements.append(Paragraph("Sales of Different Products with ABC Classification:", styles['Heading2']))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph("Graph showing sales of different products labeled with their ABC classification:", styles['Normal']))
        elements.append(Spacer(1, 12))
        elements.append(product_sales_graph_image)

        # Add report generation info
        generated_info = f"Report Generated on: {datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')}\nReport Generated by: Rheiniel Damasco"
        generated_info_para = Paragraph(generated_info, styles['Normal'])
        elements.append(Spacer(1, 24))
        elements.append(generated_info_para)

        pdf.build(elements)
        print(f"PDF saved as '{pdf_filename}'")

    def generate_product_sales_graph(self, df_classification):
        # Generate a graph of sales of different products with ABC classification labels
        plt.figure(figsize=(10, 6))

        # Plot data
        for category, color in zip(['A', 'B', 'C'], ['#606C38', '#283618', '#ABE27D']):
            subset = df_classification[df_classification['Category'] == category]
            plt.bar(subset['ProductID'].astype(str), subset['SalesValue'], label=f'Category {category}', color=color)

        plt.xlabel('Product ID')
        plt.ylabel('Sales Value')
        plt.title('Sales of Different Products with ABC Classification')
        plt.legend()

        # Save plot to buffer
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plt.close()

        return buffer