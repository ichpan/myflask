#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from application.settings import Config


class MailServer:

    def __init__(self):
        self.email = Config.MAIL_ID
        self.password = Config.MAIL_PWD
        self.smtp_server = Config.MAIL_SMTP_SERVER
        self.smtp_port = Config.MAIL_SMTP_PORT

    def send_email(self, to_email, subject, body):
        # create a MIMEMultipart example and set mail headers info.
        message = MIMEMultipart()
        message["From"] = self.email
        message["To"] = to_email
        message["Subject"] = subject

        # add text content to MIMEText example
        message.attach(MIMEText(body, "plain"))

        # create client
        smtp_client = smtplib.SMTP(self.smtp_server, self.smtp_port)
        smtp_client.starttls()
        smtp_client.login(self.email, self.password)
        smtp_client.sendmail(self.email, to_email, message.as_string())

        # close server.
        smtp_client.quit()
