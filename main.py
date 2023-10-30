import os
import random
from slack_sdk import WebClient
from datetime import datetime


# Initialize the Slack client
slack_token = os.environ['SLACK_USER_TOKEN']
client = WebClient(token=slack_token)

if ( datetime.today().weekday() != 5 and datetime.today().weekday() != 6 ):

    # Define your morning and evening messages
    morning_messages = [
        "Front End Part in apothecary repo",
        "Front End Part in operation dash board  ",
        "Front End Part in patient app  ",
        "Front End Part in Front Desk Dash board  ",
        "Front End Part in Offline web emr repository",
        "back end Part in apothecary service",
        "back end Part in apothecary emr service",
    ]

    today_date = datetime.today().strftime("%d %B %Y")
    random_minute =  str(random.randint(1,30))
    pre_defined_text = "Working on "
    random_message = random.choice(morning_messages)

    final_message = f'''DATE :- {today_date} 
    SOD  10:{random_minute} AM
    Plan Of the day: 
    { pre_defined_text } {random_message}
    '''

    # Send a message as your personal Slack account
    def send_slack_message(message):
        client.chat_postMessage(channel=os.environ['SLACK_CHANNEL'], text=message)

    send_slack_message(final_message)
