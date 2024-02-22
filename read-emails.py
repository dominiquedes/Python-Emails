from simplegmail import Gmail
from simplegmail.query import construct_query

gmail = Gmail()


params = {
    "in": "starred",
    "newer_than": (6, "month")
}

messages = gmail.get_messages(query=construct_query(params))

for message in messages: 
    print("From: " + message.sender + "About: " + message.subject)
    print(message.snippet)

