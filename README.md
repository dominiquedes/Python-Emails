# Python Emails
I often struggle with navigating through Gmail. I find it tiring to scroll through useless emails, and even though I can set filters, they're never fully effective. Therefore, I am working on my new big focus, the ultimate terminal Gmail assistant. I plan to do all of this in Python, and when it's all finished, I will attempt to make it into an application.

## Phase 1: Reading Emails
I first began my project in creating the ultimate terminal gmail assistant by first creating the email fetching component. I plan on using [simplegmail](https://github.com/jeremyephron/simplegmail/blob/master/simplegmail/query.py) for the Gmail proportion of the project; when learning to get the emails it proved to be easy and clear-cut on what to do. I used the queries provided to set the instructions for fetching my emails: starred and no older than six months. I experimented with the other parameters, but this was the most useful. 

## Phase 2: Sending Emails 
The sending part was easy since they gave you the instructions in the documentation. You can choose what you want to include and modify the information. I kept the essentials (to, subject, sender), but decided to use HTML for the message instead of plain text. My decision was based on my knowledge of HTML and the ability to customize the text. In the future, I plan to add the OpenAi bot to draft emails. This idea came across to me on Youtube, the programmer uses simplegmail and OpenAI to write emails for him using the prompt given. 

[Click this link to watch the video](https://www.youtube.com/watch?v=rT_SMx1elQ4&ab_channel=iansamir)
