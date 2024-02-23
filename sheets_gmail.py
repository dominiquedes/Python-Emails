import gspread
from oauth2client.service_account import ServiceAccountCredentials
from simplegmail import Gmail
from simplegmail.query import construct_query
from datetime import date


gmail = Gmail()

subject = input("What should the email subject include?")
sender = input("What is the sender's email?")
attachment = input("Is there an attachment in the email? (yes/no)")
older_than = input("How many days after today do you want these emails to come from?")
newer_than = input("How many days ago do you want the emails from?")
before = input("Before what date do you want these emails to come from?(year/month/day)")
after = input("After what date do you want these emails to come from?(year/month/day)")

params = {}

if subject != "":
    params["subject"] = subject
if sender != "":
    params["sender"] = sender
if attachment == "yes":
    params["attachment"] = True
if older_than != "" and newer_than == "":
    params["older_than"] = (older_than, "day")
if newer_than != "" and older_than == "": 
    params["newer_than"] = (newer_than, "day")
if before != "":
    params["before"] = before
if after != "":
    params["after"] = after 

print(params)

messages = gmail.get_messages(query=construct_query(params))

print(len(messages))

def create_new_sheet(sheet_name):

    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
    
    client = gspread.authorize(creds)
    
    folder_id = '1v2XXofNYxk7ypPJ_KaOqzT3GA5wNpkNx'
    new_sheet = client.create(sheet_name, folder_id=folder_id)
    
    return new_sheet

current_date = date.today()
current_date_str = current_date.strftime("%Y-%m-%d")
print(current_date)

new_sheet = create_new_sheet("Emails Filtered: " + current_date_str)

def add_data(sheet_id):
    scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)

    gc = gspread.authorize(credentials)

    
    sheet = gc.open_by_key(sheet_id)

    worksheet = sheet.get_worksheet(0)  

    for i, message in enumerate(messages, start=1):
        worksheet.update_cell(i, 1, message.date)
        worksheet.update_cell(i, 2, message.sender)
        worksheet.update_cell(i, 3, message.subject)

    print("Data added successfully!")

add_data(new_sheet.id)

