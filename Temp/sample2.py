import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

def on_button_clicked():
    label.setText("Button Clicked!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('QPushButton Properties Example')

    layout = QVBoxLayout()
    window.setLayout(layout)

    # Create a label to display messages
    label = QLabel("Click the button...")
    layout.addWidget(label)

    # Create a horizontal layout for the button and checkbox
    button_layout = QHBoxLayout()

    # Create a QPushButton
    button = QPushButton('Click Me')
    button.setToolTip('This is a QPushButton')
    button.setIcon(QIcon('icon.png'))  # Set an icon
    button.setIconSize(QSize(24, 24))  # Set icon size

    # Set button properties
    button.setFixedSize(QSize(150, 50))  # Set fixed size
    button.setCheckable(True)  # Make the button checkable
    button.setChecked(False)  # Initially unchecked
    button.setDefault(False)  # Not the default button in a dialog

    # Connect button signal to slot
    button.clicked.connect(on_button_clicked)

    # Add button to the layout
    button_layout.addWidget(button)
    layout.addLayout(button_layout)

    window.show()
    sys.exit(app.exec_())
