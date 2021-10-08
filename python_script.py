# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# import the smtplib module. It should be included in Python by default
import smtplib

from string import Template

import time

# set up the SMTP server
s = smtplib.SMTP(host='Put host address here', port=123) # Update port 
s.starttls()
s.login("Put email here", "Put password here")

# Function to read the contacts from a given contact file and return a
# list of names and email addresses
def get_contacts(filename):
    emails = []
    links = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            emails.append(a_contact.split()[0])
            links.append(a_contact.split()[1])
    return emails, links


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

emails, links = get_contacts('my_details.txt') # read contacts
message_template = read_template('message.txt')

# For each contact, send the email:
for email, link in zip(emails, links):
    print(email)
    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template
    message = message_template.substitute(email=email, link=link)

    # setup the parameters of the message
    msg['From']="Put sender's name here"
    msg['To']=email
    msg['Subject']="Put subject here"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    s.send_message(msg)
    
    del msg
    print("Done!")
    time.sleep(5)