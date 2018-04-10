#!/usr/bin/python3
#-*- coding: utf-8 -*-
import os, time
from lxml import etree
from Webhook.Webhook import Sdtdhook

webhook_url = 'https://discordapp.com/api/webhooks/id/token'
webhook_server_ip = '127.0.0.1'
    
if __name__ == '__main__':
    instances = []
    instancesDir = '/home/sdtd/instances'
    if os.path.isdir(instancesDir) == True:
        while True:
            for instance in os.listdir(instancesDir):
                instanceConf = '{}/{}/config.xml'.format(instancesDir, instance)
                if os.path.exists(instanceConf) == True:
                    doc = etree.parse()
                    root = doc.getroot()
                    for child in root:
                        if child.attrib['name'] == 'ServerName':
                            servername = child.attrib['value']
                        if child.attrib['name'] == 'ServerPort':
                            port = int(child.attrib['value'])
                    instances.append(Sdtdhook(webhook_server_ip, port, servername, webhook_url))
                else:
                    print('Instance not valid')
            while True:
                for instance in instances:
                    # Send message if server state changes
                    instance.process()
                time.sleep(10)
    else:
        print('Instances folder not found!')