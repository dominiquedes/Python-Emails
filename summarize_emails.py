from simplegmail import Gmail
from openai import OpenAI
from simplegmail.query import construct_query

API_KEY = ''

client = OpenAI(
    api_key=API_KEY,
)

gmail = Gmail()

subject = input("What is the subject of the email you would like to summarize?")

params = {
    'subject': subject,
}

message = gmail.get_messages(query=construct_query(params))

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a excellent english summarizer, you are able to read huge information and condense it to something short and simpe"},
        {"role": "user", "content": f'Summarize this informatin into a 1 paragraph: {message[0].plain}'}  
    ]
)

print(completion.choices[0].message.content)
