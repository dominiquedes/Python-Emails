from simplegmail import Gmail

gmail = Gmail()

to = input("Who would you like to send the email to? \n")
subject = input("What is the subject of the emai?\n")
html = input("Enter html email: \n")

params = {
    "to": to,
    "sender": "dominiquedesertb@gmail.com",
    "subject": subject,
    "msg_html": html, 
}

message = gmail.send_message(**params)

print("\n Message Sent")