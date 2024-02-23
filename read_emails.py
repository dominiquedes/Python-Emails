from simplegmail import Gmail
from simplegmail.query import construct_query

# Uses google authentication to get the user
gmail = Gmail()

# Gets emails that are no older than 6 months in the starred folder
params = {
    "in": "starred",
    "newer_than": (6, "month")
}

# Runs the function with the instructions stated above
messages = gmail.get_messages(query=construct_query(params))

# for each message in messages it give the sender and the subject along with a short snippet of the email
for message in messages: 
    print("From: " + message.sender + "About: " + message.subject)
    print(message.snippet)

