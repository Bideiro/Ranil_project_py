import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class TableDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTableWidget Example')
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['Header 1', 'Header 2', 'Header 3'])

        # Add some items
        for i in range(4):
            for j in range(3):
                self.tableWidget.setItem(i, j, QTableWidgetItem(f'Item {i+1},{j+1}'))

        # Connect the itemDoubleClicked signal to the function
        self.tableWidget.itemDoubleClicked.connect(self.on_item_double_click)

        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

    def on_item_double_click(self, item):
        row = item.row()
        column_count = self.tableWidget.columnCount()

        # Collect all items in the row
        row_data = []
        for column in range(column_count):
            cell_item = self.tableWidget.item(row, column)
            if cell_item:
                row_data.append(cell_item.text())
            else:
                row_data.append('')  # Handle empty cells

        # Print the whole row's data
        print(f'Double clicked on row {row+1}: {row_data}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = TableDemo()
    demo.show()
    sys.exit(app.exec_())
