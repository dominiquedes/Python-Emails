# Python Emails
I often struggle with navigating through Gmail. I find it tiring to scroll through useless emails, and even though I can set filters, they're never fully effective. Therefore, I am working on my new big focus, the ultimate terminal Gmail assistant. I plan to do all of this in Python, and when it's all finished, I will attempt to make it into an application.

## Phase 1: Reading Emails
I first began my project in creating the ultimate terminal gmail assistant by first creating the email fetching component. I plan on using [simplegmail](https://github.com/jeremyephron/simplegmail/blob/master/simplegmail/query.py) for the Gmail proportion of the project; when learning to get the emails it proved to be easy and clear-cut on what to do. I used the queries provided to set the instructions for fetching my emails: starred and no older than six months. I experimented with the other parameters, but this was the most useful. 

## Phase 2: Sending Emails 
The sending part was easy since they gave you the instructions in the documentation. You can choose what you want to include and modify the information. I kept the essentials (to, subject, sender), but decided to use HTML for the message instead of plain text. My decision was based on my knowledge of HTML and the ability to customize the text. In the future, I plan to add the OpenAi bot to draft emails. This idea came across to me on Youtube, the programmer uses simplegmail and OpenAI to write emails for him using the prompt given. 

[Click this link to watch the video](https://www.youtube.com/watch?v=rT_SMx1elQ4&ab_channel=iansamir)

## Phase 3: Google Sheets and Emails
This component was the most challenging. I had to learn how to use the sheets API, which was confusing due to how complex the documentation was, and then learn how to handle the large chunks of information. It started easy, creating the inputs and getting the messages, but then the Google Sheets component stumped me. The first challenge I faced was learning how to create a Google sheet; I asked ChatGPT how to start, but the information given wasn't helpful. I then went to YouTube, where I found a video (I forgot the name) displaying the steps. I learned that it wasn't only the Google Sheets API that needed to be enabled but also the Google Drive API so that it could have access to the folder, which was shared with the service account, to create the Google Sheets. I then had to learn how to add the data; the first half was authorizing, and afterward, I struggled with the second half. I had to turn to ChatGPT for help, and the information given was efficacious. From this, I learned that ChatGPT will not always be reliable, which taught me how to overcome challenges.

## Phase 4: Using OpenAI to Summarize Emails
To summarize a given email, the computer needs an indication of the email. I used the email's subject to indicate which email to summarize. OpenAI guides you on how to use the API and gives the user example code. So, I used the example code given to create the system's role and made a template for the emails. Overall, this was very simple, displaying how useful the OpenAI is and how applicable it is to website application
