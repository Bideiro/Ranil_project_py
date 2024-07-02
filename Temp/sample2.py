import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from pathlib import Path
import fitz  # Importing fitz from PyMuPDF

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PDF Viewer')
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget and a layout for it
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Create a button to open PDF file
        self.button_open_pdf = QPushButton('Open PDF')
        self.button_open_pdf.clicked.connect(self.open_pdf)
        self.layout.addWidget(self.button_open_pdf)

        # Create a web engine view to display PDF (alternative method)
        self.webview = QWebEngineView()
        self.layout.addWidget(self.webview)

    def open_pdf(self):
        try:
            # Assuming the PDF file is named 'example.pdf' in the same directory
            file_name = 'example.pdf'  # Replace with your file name or full path
            
            # Get the full path to the PDF file
            pdf_path = Path(__file__).resolve().parent / file_name
            
            # Use PyMuPDF (fitz) to render PDF page as image
            doc = fitz.open(str(pdf_path))
            page = doc.load_page(0)  # Load first page
            
            # Render page to pixmap
            pixmap = page.get_pixmap()
            
            # Save pixmap to a temporary image file (PNG)
            temp_image_path = str(pdf_path.with_suffix('.png'))
            pixmap.writePNG(temp_image_path)
            
            # Load the temporary image file into QWebEngineView
            self.webview.setUrl(QUrl.fromLocalFile(temp_image_path))

        except Exception as e:
            print(f"Error loading PDF: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
