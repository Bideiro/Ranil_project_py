from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Vertical Layout Example')

layout = QVBoxLayout()

button1 = QPushButton('Button 1')
label = QLabel('Label')
button2 = QPushButton('Button 2')


layout.addWidget(label)
layout.addWidget(button1)

layout.addWidget(button2)

window.setLayout(layout)

window.show()
sys.exit(app.exec_())
