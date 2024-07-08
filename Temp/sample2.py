import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QSizeF

class PrintWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel('This is a sample text to print.', self)
        layout.addWidget(self.label)

        self.print_button = QPushButton('Print', self)
        self.print_button.clicked.connect(self.handlePrint)
        layout.addWidget(self.print_button)

        self.preview_button = QPushButton('Print Preview', self)
        self.preview_button.clicked.connect(self.handlePrintPreview)
        layout.addWidget(self.preview_button)

        self.setLayout(layout)
        self.setWindowTitle('Print Widget Example')
        self.setGeometry(100, 100, 400, 300)

    def handlePrint(self):
        printer = QPrinter()
        printer.setResolution(300)  # Set high resolution

        print_dialog = QPrintDialog(printer, self)
        if print_dialog.exec_() == QPrintDialog.Accepted:
            self.printContent(printer)

    def handlePrintPreview(self):
        printer = QPrinter()
        printer.setResolution(300)  # Set high resolution
        preview_dialog = QPrintPreviewDialog(printer, self)
        preview_dialog.paintRequested.connect(self.printContent)
        preview_dialog.exec_()

    def printContent(self, printer):
        # Get the size of the widget
        widget_size = self.label.size()
        
        # Convert widget size to points (1 inch = 72 points)
        dpi = printer.resolution()
        width_points = widget_size.width() * 72 / self.logicalDpiX()
        height_points = widget_size.height() * 72 / self.logicalDpiY()
        printer.setPaperSize(QSizeF(width_points, height_points), QPrinter.Point)
        printer.setFullPage(True)
        
        # Set margins to zero
        printer.setPageMargins(0, 0, 0, 0, QPrinter.Point)
        
        # Create a QPainter and set it to the printer
        painter = QPainter(printer)
        
        # Scale the painter to match the printer resolution
        scale_x = dpi / self.logicalDpiX()
        scale_y = dpi / self.logicalDpiY()
        painter.scale(scale_x, scale_y)
        
        # Render the specific widget (self.label in this case)
        self.label.render(painter)
        
        # End the painter to finalize the printing
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PrintWidget()
    window.show()
    sys.exit(app.exec_())
