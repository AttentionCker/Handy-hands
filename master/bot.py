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
from meet import grouping
from pnr import getpnr
from jobs import getjobs
from currency import fetch_currency_exchange_rate
from weather import get_weather
from joke import lame_jokes
from translate import translate_message
from hack import eventz

# files for bot controlled
from labour import Component_bot
from labour import Connection_tester_bot
from labour import Solder_bot
from labour import IC_bot


BOT_MAIL = "master-bot@zulipchat.com"

# Brings the circuit board
class Master(object):

    def __init__(self):
        self.client = zulip.Client(config_file="../master.zuliprc")
        print("Master Bot at work to controll you all...")
        
        # client_list = self.client.get_members()
        # print("\nClients in the org : ")
        # print(type(client_list))
        # for name in range(len(client_list)):
        #     print(client_list['members'][name]['full_name'])

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
        if content[0].lower() == "@**master**" or content[0].lower() == "master":
            message = ""

            
            # task keywords for slaves
            task1 = ["task1", "connections"]
            task2 = ["task2", "connect-resistor", "connect circuit", "connect LED", "connect capacitor", "built ciruit"]
            task3 = ["task 3", "solder"]
            task4 = ["task4", "connect-IC"]
            greet = ["hello", "hi","hola","hey","wassup"]
            news = ["news", "happenings today"]

            # PERFORMING SPECIFIC COMMANDS
                
            # GREETINGS
            # when hello/hi in the first sections of the content 
            # looking through entire test will take longer
            
            if content[1].lower() in greet:
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

            # MEETUP DETAILS
            elif content[1].lower() == "meetup":
                name = ""
                for i in range(2,len(content)-1):
                    name+=content[i]
                    name+=" "
                name+=content[len(content)-1]
                
                dicti = grouping(name)
                message += "**MeetUp Event Details**" + '\n'
                message += "Name: " + dicti["Name"] + '\n'
                message += "Organizer: " + dicti["Organizer"] + '\n'
                message += "City: " + dicti["City"] + '\n'
                message += "Next Event: " + dicti["Upcoming Event"]["Event Name"] + '\n'
                message += "RSVP: " + str(dicti["Upcoming Event"]["RSVP"]) + '\n'
                message += "Time: " + dicti["Upcoming Event"]["Time"] + '\n'
                message += "Link: " + dicti["Link"] + '\n'
            
            # PNR DETAILS
            elif content[1].lower() == "pnr":
                num = int(content[2])
                try:
                    message = getpnr(num)
                except:
                    message = "Try valid PNR"

            # TRANSLATE FUNCTION
            elif content[1].lower() == "translate":
                try:
                    message = content[2:]
                    message = " ".join(message)
                    message = translate_message(message)
                except:
                    message = "Error in format"

            # GIVES AVAILABLE JOBS DETAILS
            elif content[1].lower() == "jobs":
                try:
                    message = getjobs()
                except:
                    message = "Connection Error"

            # 
            elif content[1].lower() == "currency":
                if len(content) == 3 and content[2].lower() != "":
                   
                    currency = fetch_currency_exchange_rate("", content[2].upper())
                    message += "**Showing all currency conversions for 1 {}:**\n".format(content[2].upper())
                    for curr in currency['rates']:
                        message += "1 {} = ".format(content[2].upper()) + "{}".format(format(currency['rates'][curr], '.2f')) + " {}\n".format(curr)
                    message += "Last Updated: *{}*".format(currency['date'])
                elif len(content) == 5 and content[2].lower() != "" and content[4].lower() != "":
                   
                    currency = fetch_currency_exchange_rate(content[2].upper(), content[4].upper())
                    message += "1 {} = ".format(content[4].upper()) + "{}".format(format(currency['rates'][content[2].upper()], '.2f')) + " {}\n".format(content[4].upper())
                    message += "Last Updated: *{}*".format(currency['date'])
                else:
                    message = "Please ask the query in correct format."

            # TELLS JOKE
            elif content[1].lower() == "joke":
                try:
                    message = lame_jokes()
                except:
                    message = "Not that lame though .. try something else"

            # WEATHER DETAILS
            elif content[1].lower() == "weather":
                try:
                    if len(content) > 2 and content[2].lower() != "":
                        
                        weather = get_weather(content[2].lower())
                        if str(weather['cod']) != "404":
                            message += "**Weather status of {}**\n".format(content[2].lower())
                            message += "Climate: **{}**\n".format(str(weather['weather'][0]['description']))
                            message += "Temperature: **{}**\n".format(str(weather['main']['temp'] - 273) + "° C")
                            message += "Pressure: **{}**\n".format(str(weather['main']['pressure']) + " hPa")
                            message += "Humidity: **{}**\n".format(str(weather['main']['humidity']) + "%")
                            message += "Wind Speed: **{}**".format(str(weather['wind']['speed']) + " $$m/s^2$$")
                        else:
                            message = "City not found!\nabc"
                    else:
                        message = "Please add a location name."
                except:
                    message = "Something went wrong"

            # CONTEST DETAILS
            elif content[1].lower() == "contest":
                try:
                    message = eventz()
                except:
                    message = "Check connection"
                
        
            # CONTROL OF OTHER BOTS
            # MASTER BOT CALLS THE SLAVE BOTS FOR WORK.

            # Respective slave objects will be called reading the specified task
            elif content[1].lower() in task1:
                # call slave 1
                s1 = Connection_tester_bot()
                s1.process(msg)

            elif content[1].lower() in task2:
                # call slave 2
                s2 = Component_bot()
                s2.client.call_on_each_message(s2.process)

            elif content[1].lower() in task3:
                # call slave 3
                s3 = Solder_bot()
                s3.client.call_on_each_message(s3.process)

            elif content[1].lower() in task4:
                s4 = IC_bot()
                s4.client.call_on_each_message(s4.process)

            else:
                message += "Show news according to your choice : **Master news topic-name**\n"
                message += "Show MeetUp group details and next event status : **Master meetup group-name**\n"
                message += "Crack a joke ... even a lame one : **Master joke**\n"
                message += "Get the current currency conversion ratios : **Master currency currency-1 to currency-2** \nor **Master currency currency-1** \n"
                message += "Get a list of upcoming coding events: **Master contest**\n"
                message += "Get weather status of a location: **Master weather location**\n"
                message += "Get a list of new job openings in your locality: **Master jobs**\n"
                message += "Translate a word or sentence to English: **Master translate word/sentence**\n"
                message += "Check your pnr status: **Master pnr pnr-number**\n"

           
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
