import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QScrollArea, QGridLayout, QSizePolicy

class DynamicButtonApp(QMainWindow):
    def __init__(self, button_labels):
        super().__init__()
        self.setWindowTitle('Custom Styled Dynamic Button App')
        self.setGeometry(100, 100, 400, 300)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main layout for the central widget
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        main_layout.addWidget(scroll_area)

        # Container widget for the scroll area
        container_widget = QWidget()
        scroll_area.setWidget(container_widget)

        # Grid layout for the buttons
        grid_layout = QGridLayout()
        container_widget.setLayout(grid_layout)

        # Dynamically create buttons and add to the grid layout
        for i, label in enumerate(button_labels):
            button = QPushButton(label)
            button.clicked.connect(self.on_button_click)
            button.setProperty('buttonNumber', i + 1)  # Store the button's index as a custom property
            row = i // 3
            col = i % 3
            grid_layout.addWidget(button, row, col)


            # Set size policy to fixed so the button won't resize
            button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    def on_button_click(self):
        sender = self.sender()
        button_number = sender.property('buttonNumber')
        print(f'Button {button_number} ({sender.text()}) clicked')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # List of labels for buttons
    button_labels = ['Button 1', 'Button 2', 'Button 3', 'Button 4', 'Button 5', 'Button 6', 'Button 7', 'Button 8', 'Button 9', 'Button 10']

    # Create and show the main window
    main_window = DynamicButtonApp(button_labels)
    main_window.show()

    sys.exit(app.exec_())
