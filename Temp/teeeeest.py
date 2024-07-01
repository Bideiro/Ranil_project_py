import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLabel

class InnerWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.label = QLabel('Inner Widget')
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        
        self.setLayout(layout)

class OuterWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.inner_widget = InnerWidget()
        
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Outer Widget'))
        layout.addWidget(self.inner_widget)
        
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    outer_widget = OuterWidget()
    outer_widget.show()
    
    sys.exit(app.exec_())
