import pprint
import zulip
import sys
import re
import json
import httplib2
import os
import math
import threading
import nltk


from topnews import getTopNews


BOT_MAIL = "master-bot@zulipchat.com"

# Brings the circuit board
class Master(object):

    def __init__(self):
        self.client = zulip.Client(config_file="../master.zuliprc")
        print("Master Bot at work to controll you all...")
        
        client_list = self.client.get_members()
        print("\nClients in the org : ")
        # print(type(client_list))
        for name in range(len(client_list)):
            print(client_list['members'][name]['full_name'])

        self.subscribe_all()

    def subscribe_all(self):
        json = self.client.get_streams()["streams"]
        # print(json)
        streams = [{"name": stream["name"]} for stream in json]
        # print stream names
        self.client.add_subscriptions(streams)

    # creating new user
    def create_slave(self):
        request = {
            'email' : 'newslave@zulip.com',
            'password': 'temp',
            'full_name' : 'new slave',
            'short_name' : 'newb'
        }

        result = self.client.create_user(request)
        print('Created a new slave to rule upon')
        print(result)

    # creating a slave
    def make_slave_realm(self):
        request = {
        'name': 'marketing',
        'description': 'The marketing team.',
        'members': [3,4,5], # to be changed
        }

        result = self.client.create_user_group(request)
        print("A new slave world created")
        print(result)

    # All process
    def process(self, msg):
        content = msg["content"].split()
        stream_name = msg["display_recipient"]

        # Master needs to be entered before specifying any task
        if content[0].lower() == "@**master**":
            message = ""

        
        # PERFORMING SPECIFIC COMMANDS
                
            # GREETINGS
            # when hello/hi in the first sections of the content 
            # looking through entire test will take longer
            greet = ["hello", "hi","hola","hey","wassup"]
            news = ["news", "happenings today"]

            if content[0].lower() in greet or content[1].lower() in greet:
                print("master is greeting")
                message = "Hola .. ever wondered why am I the master because I have the power to control you **Alll**"

            # SHOWING NEWS ITEMS
            elif "news" in content:
                topic = content[2].lower()
                try:
                    news = getTopNews(topic)
                    for i in range(10):
                        message += "**"+news[i]['title']+"**" 
                        message += '\n'
                        message += news[i]['desc']
                        message += '\n\n'
                except:
                    message = "Nothing new in the world ... Go Sleep"

           
            self.client.send_message({
                "type": "stream",
                "to": stream_name,
                "subject": msg["subject"],
                "content": message
            })

def main():
    boss = Master() # master bot that controls all
    boss.client.call_on_each_message(boss.process)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSayonara.")
        sys.exit(0)
