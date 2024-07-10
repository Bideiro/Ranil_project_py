from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtWidgets import QApplication, QTextEdit
from PyQt5.QtGui import QTextDocument
from PyQt5.QtCore import QSizeF
from PyQt5.QtWidgets import QDialog, QWidget, QVBoxLayout,QHBoxLayout ,QSpacerItem, QSizePolicy, QLabel
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QSizeF, QMarginsF

app = QApplication([])

# Create a QTextEdit widget with content
widget = QTextEdit()
widget.setPlainText("Your receipt content here")

# Set up a QTextDocument for the content
document = QTextDocument()
document.setPlainText(widget.toPlainText())

# Set up the printer
printer = QPrinter(QPrinter.HighResolution)
printer.setOutputFormat(QPrinter.NativeFormat)
printer.setPaperSize(QPrinter.Custom)
printer.setPageSize(QPrinter.Custom)
printer.setPageMargins(0, 0, 0, 0, QPrinter.Millimeter)
printer.setFullPage(True)
printer.setResolution(300)  # Adjust the resolution as needed

# Adjust paper width to 58mm
paper_width_mm = 58
paper_width_pixels = paper_width_mm / 25.4 * printer.resolution()

# Set paper size
printer.setPaperSize(QSizeF(paper_width_pixels, document.size().height()), QPrinter.DevicePixel)

# Print
dialog = QPrintDialog(printer)
if dialog.exec_() == QDialog.Accepted:
    painter = QPainter(printer)
    document.drawContents(painter)
    painter.end()
