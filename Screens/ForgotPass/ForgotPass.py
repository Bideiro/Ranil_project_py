import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QInputDialog
from PyQt5 import QtCore
from .ForgotPass_ui import Ui_MainWindow  # Replace with your UI file import
from Dialogs.DLog_InputAdminPasscode import DLG_Change

class ForgotPassWindow(QMainWindow, Ui_MainWindow):
    
    back = QtCore.pyqtSignal()
    
    def __init__(self):
        super(ForgotPassWindow, self).__init__()
        self.setupUi(self)
        self.send_btn.clicked.connect(self.on_send_btn_clicked)  # Connect send button click to handler
        self.user_input = None

    @QtCore.pyqtSlot()
    def on_back_btn_clicked(self):
        print("Back button clicked")
        self.back.emit()
    
    def generate_otp(self):
        # Generate a 6-digit random OTP
        return str(random.randint(100000, 999999))  # Convert OTP to string for comparison
    
    def on_send_btn_clicked(self):
        # Fetch user and email inputs (assuming you have self.user_LE and self.email_LE)
        self.user_input = self.user_LE.text()
        receiver_email = self.email_LE.text()

        # Generate OTP and send OTP email
        otp = self.generate_otp()
        self.send_otp_email(receiver_email, otp)

        # Open a dialog to get OTP from user
        user_otp, ok_pressed = QInputDialog.getText(self, "OTP Verification", "Enter the OTP sent to your email:")
        
        if ok_pressed:
            if user_otp == otp:
                QMessageBox.information(self, "Success", "OTP matched. Proceed to reset password.")
                # Emit signal or handle UI feedback for successful OTP verification
                self.showResetPassWindow()
                self.back.emit()
            else:
                QMessageBox.warning(self, "Error", "OTP does not match. Please try again.")

    def send_otp_email(self, receiver_email, otp):
        sender_email = 'raineeyd@gmail.com'
        password = 'xfmx wybe mpyx swhm'

        subject = 'OTP for Verification'
        body = f'Your OTP for verification is: {otp}'

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            server.quit()
            print("Success: OTP sent successfully")
        except smtplib.SMTPException as e:
            print(f"Error: {e}")

    def showResetPassWindow(self):
        from Screens.ForgotPass import ForgotPassWindow
        Reset_Pass_Window = DLG_Change(userName=self.user_LE.text())
        Reset_Pass_Window.exec()

