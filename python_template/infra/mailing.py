"""Implement a class to send email."""

import logging
import mimetypes
import os
import smtplib
import ssl
from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

logger = logging.getLogger(__name__)


class Mailing:
    """
    Create a mailer object that can send emails.

    Parameters
    ----------
    host: str
        smtp server host (recommanded value: 'smtp-auth.mpsa.com')
    sender: str
        email address of sender (ex: 'benjamin.habert@ext.mpsa.com')
    user: str
        RPI account name of sender (ex: 'u542013'). **NOTE**: this account
        has to match the email address.
    password: str
        RPI password for the provided user
    topic: str
        (optional) prepend all the messages sent by this topic. Usefull
        to provide the application name.
    receivers: list of str
        (optional) email addresses that will receive all the emails


    Example
    -------

        >>> mailing_config = {
                'host': '',
                'sender': '',
                'user': '',    # RPI account - has to match the sender email address
                'password': '*****',  # RPI password
                'topic': '[myapp][prod]',    # default topic of all mails sent, optional
                'receivers': ['']
            }
        >>> mailer = Mailer(**mailing_config)
        >>> mailer.send(
                'starting!',    # additional topic. Topic will thus be: "[myapp][prod] starting!"
                "Job started on machine xx at time yyy."  # body of the message
            )
        >>> ...
        >>> mailer.send(
                'error!',
                'Job XXX created the following error : ...',
                receivers=[''],  # optional additional receiver of email
                attachments=['/path/to/data.xlsx', '/path/to/logs.txt']  # optional: attach files
            )

    """

    def __init__(self, servers, sender, topic="", receivers=None):
        """Initiate the class instance."""
        self.host = ""
        self.port = 587
        self.user = ""
        self.login = False
        self.servers = servers
        self.sender = sender
        self.password = ""
        self.topic = topic
        self.receivers = [] if receivers is None else receivers
        self.check_smtp_connection()

    def check_smtp_connection(self):
        """Check if connection to SMTP can be established."""
        self.servers = [self.servers] if not isinstance(self.servers, list) else self.servers
        for server_pos, server in enumerate(self.servers):
            logging.info(f"Trying a connection to SMTP Server: {server['SMTP_SERVER']}")
            try:
                with smtplib.SMTP(server["SMTP_SERVER"], server["SMTP_PORT"]) as s:
                    s.starttls()
                    if server["SMTP_LOGIN"]:
                        s.login(server["SMTP_USERNAME"], self.password)
                    self.host = server["SMTP_SERVER"]
                    self.port = server["SMTP_PORT"]
                    self.user = server["SMTP_USERNAME"]
                    self.password = server["SMTP_PASSWORD"]
                    self.login = server["SMTP_LOGIN"]
                    return True
            except (smtplib.SMTPException, Exception) as e:
                logging.info(f"Error connecting to the SMTP server: {e}")
                if server_pos + 1 >= len(self.servers):
                    raise

    def send(self, topic, message, receivers=None, attachments=None):
        """Send email message to receivers' addresses.

        Parameters
        ----------
        topic: str
            additional detail for topic of email (added to the topic provided to the class)
        message: str
            body of the email
        receivers: list of str
            (optional) additional receivers (email addresses to send to).
        attachments: list of str
            (optional) list of abspath to files to attach to the message.
        """
        full_topic = (self.topic + " " + topic).strip()
        full_receivers = list(set(([] if receivers is None else receivers) + self.receivers))
        if not full_receivers:
            raise ValueError("You must specify at least one receiver - either when creating " "the Mailer object or when using the .send() function.")
        msg = MIMEMultipart("mixed")

        # msg = MIMEText()
        msg["Subject"] = full_topic
        msg["From"] = self.sender
        msg["To"] = "; ".join(full_receivers)
        msg.attach(MIMEText(message, "html", "utf-8"))
        if attachments:
            for path in attachments:
                self.add_attachment_to_message(msg, path)

        msg_text = msg.as_string()
        s = smtplib.SMTP(self.host, port=self.port)
        ssl_context = ssl._create_unverified_context()
        s.starttls(context=ssl_context)
        s.ehlo()
        if self.login:
            s.login(self.user, self.password)
        s.sendmail(self.sender, full_receivers, msg_text)
        s.quit()

    @staticmethod
    def add_attachment_to_message(main_message, attachment_path):
        """Attach file (from absolute path) to a MIMEMultipart message object."""
        # copied from: https://docs.python.org/2/library/email-examples.html
        if not os.path.isfile(attachment_path):
            logging.warning("Wrong path provided as attachment: " + attachment_path)
            return
        filename = os.path.basename(attachment_path)
        # Guess the content type based on the file's extension.  Encoding
        # will be ignored, although we should check for simple things like
        # gzipped or compressed files.
        ctype, encoding = mimetypes.guess_type(attachment_path)
        if ctype is None or encoding is not None:
            # No guess could be made, or the file is encoded (compressed), so
            # use a generic bag-of-bits type.
            ctype = "application/octet-stream"
        maintype, subtype = ctype.split("/", 1)
        if maintype == "text":
            fp = open(attachment_path)
            # Note: we should handle calculating the charset
            msg = MIMEText(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == "image":
            fp = open(attachment_path, "rb")
            msg = MIMEImage(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == "audio":
            fp = open(attachment_path, "rb")
            msg = MIMEAudio(fp.read(), _subtype=subtype)
            fp.close()
        else:
            fp = open(attachment_path, "rb")
            msg = MIMEBase(maintype, subtype)
            msg.set_payload(fp.read())
            fp.close()
            # Encode the payload using Base64
            encoders.encode_base64(msg)
        # Set the filename parameter
        msg.add_header("Content-Disposition", "attachment", filename=filename)
        main_message.attach(msg)
