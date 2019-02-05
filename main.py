import requests
import time 
import datetime

token = input("Token: ")
request_params = {'token': token}

flag = True

while True:

    currentDT = datetime.datetime.now()
    response = requests.get('https://api.groupme.com/v3/groups/47904778/messages',params=request_params)

    # If there are new messages, check whether any of them are making queries to the bot
    if (response.status_code == 200):
        response_messages = response.json()['response']['messages']

        if currentDT.hour == 7 and currentDT.minute == 15 and flag:
            to_send = "Good morning! :) Where's lunch?"
            flag = False
            post_params = {
                'bot_id': 'a40c5367357321ea7549f857c2', 'text': to_send}
            requests.post(
                'https://api.groupme.com/v3/bots/post', params=post_params)

        # Iterate through each message, checking its text
        for msg in response_messages:
            if (msg['text'] == 'hi bobbit!'):
                to_send = 'hey :]'
                # Send the response to the group
                post_params = {
                    'bot_id': 'a40c5367357321ea7549f857c2', 'text': to_send}
                requests.post(
                    'https://api.groupme.com/v3/bots/post', params=post_params)
                request_params['since_id'] = msg['id']
                break
        