# import pprint
import zulip
import sys
import re
import json
import httplib2
import os
import requests
# import math
import threading
import nltk

from re import search
        
        
# slave1 activated for task1 
# Task 1 : Test connections
class Connection_tester_bot():
    
    def __init__(self):
        self.labor_bot = zulip.Client(config_file="../arm1.zuliprc")
        print("Slave1 up for work.")  
        self.BOT_MAIL = "slave1-bot@zulipchat.com"
        self.work_code = "0033"
        
    def subscribe_all(self):
        json = self.client.get_streams()["streams"]
        streams = [{"name": stream["name"]} for stream in json]
        self.client.add_subscriptions(streams)

    def process(self, msg):
        
        content = msg["content"].split()
        stream_name = msg["display_recipient"]

        message = "Hi I am arm 1 under Master Control.\nI test for Connections."
        
        print("labour bot 1 activate")
        # sending request to pi
        r = requests.get("http://iot.smayank.com/iot?id=" + self.work_code)
        print(r.status_code)

        self.labor_bot.send_message({
            "type": "stream",
            "to": stream_name,
            "subject": msg["subject"],
            "content": message
        })

# slave2 activated for task2
# Task 2 : Connect Resistor's/LED's/Capacitor's
class Component_bot():

    def __init__(self):
        self.labor_bot = zulip.Client(config_file="../arm2.zuliprc")
        print("Slave1 up for work.")  
        self.BOT_MAIL = "slave2-bot@zulipchat.com"
        self.work_code = "0045"
        
    def subscribe_all(self):
        json = self.client.get_streams()["streams"]
        streams = [{"name": stream["name"]} for stream in json]
        self.client.add_subscriptions(streams)

    def process(self, msg):
        
        content = msg["content"].split()
        stream_name = msg["display_recipient"]

        message = "Hi I am arm 2 under Master Control.\nI connnect various components like capacitor, resistor, led to the board."
        
        print("labour bot 2 activate")
        # sending request to pi
        r = requests.get("http://iot.smayank.com/iot?id=" + self.work_code)
        print(r.status_code)

        self.labor_bot.send_message({
            "type": "stream",
            "to": stream_name,
            "subject": msg["subject"],
            "content": message
        })

# slave3 activated for task3
# Task 3 : Solder
class Solder_bot():

    def __init__(self):
        self.labor_bot = zulip.Client(config_file="../arm3.zuliprc")
        print("Slave1 up for work.")  
        self.BOT_MAIL = "slave3-bot@zulipchat.com"
        self.work_code = "0067"
        
    def subscribe_all(self):
        json = self.client.get_streams()["streams"]
        streams = [{"name": stream["name"]} for stream in json]
        self.client.add_subscriptions(streams)

    def process(self, msg):
        
        content = msg["content"].split()
        stream_name = msg["display_recipient"]

        message = "Hi I am arm 3 under Master Control.\nI solder everything."
        
        print("labour bot 3 activate")
        # sending request to pi
        r = requests.get("http://iot.smayank.com/iot?id=" + self.work_code)
        print(r.status_code)

        self.labor_bot.send_message({
            "type": "stream",
            "to": stream_name,
            "subject": msg["subject"],
            "content": message
        })
# slave4 activated for task4
# Task 4 : Connecct IC's
class IC_bot():

    def __init__(self):
        self.labor_bot = zulip.Client(config_file="../arm4.zuliprc")
        print("Slave1 up for work.")  
        self.BOT_MAIL = "slave4-bot@zulipchat.com"
        self.work_code = "0094"
        
    def subscribe_all(self):
        json = self.client.get_streams()["streams"]
        streams = [{"name": stream["name"]} for stream in json]
        self.client.add_subscriptions(streams)

    def process(self, msg):
        
        content = msg["content"].split()
        stream_name = msg["display_recipient"]

        message = "Hi I am arm 4 under Master Control.\nI connects different IC's"
        
        print("labour bot 4 activate")

        # sending request to pi
        r = requests.get("http://iot.smayank.com/iot?id=" + self.work_code)
        print(r.status_code)

        self.labor_bot.send_message({
            "type": "stream",
            "to": stream_name,
            "subject": msg["subject"],
            "content": message
        })


