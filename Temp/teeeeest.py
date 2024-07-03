from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QLabel, QDialogButtonBox
from PyQt5.QtCore import Qt
import sys

class FlagDemoDialog(QDialog):
    def __init__(self, flag, description, parent=None):
        super().__init__(parent)
        self.setWindowTitle(description)
        self.setWindowFlag(flag)
        layout = QVBoxLayout()
        label = QLabel(description)
        layout.addWidget(label)
        button_box = QDialogButtonBox(QDialogButtonBox.Ok)
        button_box.accepted.connect(self.accept)
        layout.addWidget(button_box)
        self.setLayout(layout)

class MainDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window Flags Demo")
        layout = QVBoxLayout()
        flags = [
            (Qt.Widget, "Qt.Widget: A normal widget."),
            (Qt.Window, "Qt.Window: A window."),
            (Qt.Dialog, "Qt.Dialog: A dialog."),
            (Qt.Sheet, "Qt.Sheet: A sheet window (macOS)."),
            (Qt.Drawer, "Qt.Drawer: A drawer window (macOS)."),
            (Qt.Popup, "Qt.Popup: A pop-up window."),
            (Qt.Tool, "Qt.Tool: A tool window."),
            (Qt.ToolTip, "Qt.ToolTip: A tooltip window."),
            (Qt.SplashScreen, "Qt.SplashScreen: A splash screen."),
            (Qt.Desktop, "Qt.Desktop: The desktop."),
            (Qt.SubWindow, "Qt.SubWindow: A subwindow."),
            (Qt.MSWindowsFixedSizeDialogHint, "Qt.MSWindowsFixedSizeDialogHint: Fixed size dialog (Windows).")
        ]

        for flag, description in flags:
            button = QPushButton(description)
            button.clicked.connect(lambda _, f=flag, d=description: self.show_flag_dialog(f, d))
            layout.addWidget(button)

        self.setLayout(layout)

    def show_flag_dialog(self, flag, description):
        dialog = FlagDemoDialog(flag, description, self)
        dialog.exec_()

app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())
