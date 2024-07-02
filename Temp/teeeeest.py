import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QStackedWidget, QPushButton, QSizePolicy

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Resizable Stacked Widget Example')

        # Create a stacked widget
        self.stackedWidget = QStackedWidget()

        # Widget 1
        widget1 = QWidget()
        layout1 = QVBoxLayout()
        label1 = QLabel('Widget 1 with some content.')
        layout1.addWidget(label1)
        widget1.setLayout(layout1)
        widget1.setMinimumSize(200, 100)  # Set minimum size for widget 1
        widget1.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.stackedWidget.addWidget(widget1)

        # Widget 2
        widget2 = QWidget()
        layout2 = QVBoxLayout()
        label2 = QLabel('Widget 2 with different content that requires more space.')
        layout2.addWidget(label2)
        widget2.setLayout(layout2)
        widget2.setMinimumSize(300, 150)  # Set minimum size for widget 2
        widget2.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.stackedWidget.addWidget(widget2)

        # Button to switch widgets
        self.button = QPushButton('Switch Widget')
        self.button.clicked.connect(self.switchWidget)

        # Layout for central widget
        centralWidget = QWidget()
        centralLayout = QVBoxLayout()
        centralLayout.addWidget(self.button)
        centralLayout.addWidget(self.stackedWidget)
        centralWidget.setLayout(centralLayout)

        self.setCentralWidget(centralWidget)

    def switchWidget(self):
        # Toggle between widgets in the stacked widget
        currentIndex = self.stackedWidget.currentIndex()
        newIndex = (currentIndex + 1) % self.stackedWidget.count()
        self.stackedWidget.setCurrentIndex(newIndex)

        # Adjust window size based on the current widget's size hint
        self.adjustSize()

    def adjustSize(self):
        # Adjust the main window size based on the current widget's size hint
        currentWidget = self.stackedWidget.currentWidget()
        self.resize(currentWidget.minimumSizeHint())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
