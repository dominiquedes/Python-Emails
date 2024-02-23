from simplegmail import Gmail
from simplegmail.query import construct_query
from simplegmail.label import Label
from simplegmail import label

gmail = Gmail()


days=input("Give the number of days ago you want to fetch the emails from: (the number of days back from today)")

params = {
    "newer_than": (days, "day"),
    "category": "Primary"
}


print ("Getting messages")

messages = gmail.get_messages(query=construct_query(params))

for message in messages: 
    print("ID: \n"+ message.id )
    print("Subject"+ message.subject)
    print("Sender"+message.sender)
    print("Preview"+message.snippet+"\n")


id_to_star = input("Give me the subject of the email: ")

params_starrerd = {
    "newer_than": (days, "day"),
    "category": "Primary",
    "subject": id_to_star,
}

messages_to_loop = gmail.get_messages(query=construct_query(params_starrerd))

print(messages_to_loop)
for message in messages_to_loop:
    message.add_label(label.STARRED)