import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QInputDialog
from PyQt5 import QtCore



from .ForgotPass_ui import Ui_MainWindow
from Database.DBController import dbcont

from Dialogs.DLog_AdminPasscode import DLG_AdminPass
from Dialogs.DLog_Oneline_Input import DLG_Oneline_Input
from Dialogs.DLog_Alert import DLG_Alert

class ForgotPassWindow(QMainWindow, Ui_MainWindow):
    
    back_btnsgl = QtCore.pyqtSignal()
    
    def __init__(self):
        super(ForgotPassWindow, self).__init__()
        self.setupUi(self)
        self.otp = None
        self.db = dbcont('admin', 123456)
        self.send_btn.clicked.connect(self.validate_creds)
        self.back_btn.clicked.connect(lambda: self.back_btnsgl.emit())
        
    def validate_creds(self):
        check = self.db.get_RUID_user(uname=self.user_LE.text(), email= self.email_LE.text(),check=True)
        if check:
            self.otp_protocol()
        else:
            Dlg =DLG_Alert(msg='Not in database!')
            Dlg.exec()
    
    def otp_protocol(self):
        self.user_input = self.user_LE.text()
        self.receiver_email = self.email_LE.text()
        otp = str(random.randint(100000, 999999))
        
        if otp:
            self.send_otp_email(self.receiver_email, otp)
        
        Dlg_OI = DLG_Oneline_Input(msg= 'Enter the OTP sent to your email:')
        Dlg_OI.exec()
        
        if Dlg_OI.result() == 1:
            if Dlg_OI.Input_LE.text() == otp:
                self.showResetPassWindow()
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
            print(f'Success: OTP sent successfully: {otp}')
        except smtplib.SMTPException as e:
            print(f"Error: {e}")

    def showResetPassWindow(self):
        Dlg_ConfirmPass = DLG_AdminPass()
        Dlg_ConfirmPass.exec()
        if Dlg_ConfirmPass.result() == 1:
            self.RUID = self.db.get_RUID_user(uname=self.user_LE.text(), email= self.email_LE.text())
            self.db.update_passcode(RUID= self.RUID,passcode= Dlg_ConfirmPass.PCode_LE.text())
            Dlg = DLG_Alert()
            Dlg.exec()
            self.back_btnsgl.emit()
            
            
            

