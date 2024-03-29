# -*- coding: utf-8 -*-
"""SendCustomEmailPython.ipynb

Automatically generated by Colaboratory.
"""
# Please make sure to enter the details properly before executing the script
import smtplib
import ssl
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender_email = "Your Email goes here in quotes"
sender_name = "Your name goes in here in quotes"
password = Your_Password_Goes_here

receiver_emails = email_list
receiver_names = name_list
# Dummy Receiver and Name
# receiver_emails = ['yourid@domain.com']
# receiver_names = ['Your_name']

for receiver_email, receiver_name in zip(receiver_emails, receiver_names):

    print("Sending to " + receiver_name)
    msg = MIMEMultipart()
    msg["Subject"] = "Dummy Subject within quotes"
    msg["From"] = formataddr((sender_name, sender_email))
    msg["To"] = formataddr((receiver_name, receiver_email))

    msg.attach(
        MIMEText(
            """<h2>Hello , """
            + receiver_name
            + """</h2>
                            <p>Your custom message within p tag</p>
                            <br>
                            
                            <p>Some more text related to email if needed.</p>
                            <br>
                            <p>Provide social media handles if required</p>
                            <ul>
                                <li><a href = 'https://www.facebook.com/id/'>Facebook</a></li>
                                <li><a href = 'https://www.instagram.com/id/'>Instagram</a></li>
                            </ul>
                            <h4>Have a great day</h4>
                            """,
            "html",
        )
    )

    # You can also add custom attachment
    # filename = attachment_name + ".filetype"
    try:
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        msg.attach(part)
    except Exception as e:
        print(f"Oh no! We didnt found the attachment!n{e}")
        break

    try:
        server = smtplib.SMTP("smtp.gmail.com", 465)
        # Check internet for other service provider details.
        context = ssl.create_default_context()
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent!")
    except Exception as e:
        print(f"Oh no! Something bad happened!n{e}")
        break
    finally:
        print("Closing the server...")
        server.quit()
