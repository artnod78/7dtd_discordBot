#!/usr/bin/python3
#-*- coding: utf-8 -*-
'''
Created on 10 avr. 2018

@author: artnod
'''
import os, time
from lxml import etree
from Webhook.Webhook import Sdtdhook
from BotLog.Botlog import getBotLogger
from settings import WEBHOOK_CONF, SDTD_CONF

# Set up logger
my_logger = getBotLogger('discord_hook')

if __name__ == '__main__':
	my_logger.info('Start Discord Hook')
	instances = []
	instancesDir = '/home/sdtd/instances'
	if os.path.isdir(instancesDir) == True:
		for instance in os.listdir(instancesDir):
			instanceConf = '{}/{}/config.xml'.format(instancesDir, instance)
			if os.path.exists(instanceConf) == True:
				doc = etree.parse(instanceConf)
				root = doc.getroot()
				for child in root:
					if child.attrib['name'] == 'ServerName':
						servername = child.attrib['value']
					if child.attrib['name'] == 'ServerPort':
						port = int(child.attrib['value'])
				my_logger.debug('Add {} in instances check list'.format(instance))
				instances.append(Sdtdhook(SDTD_CONF['server_ip'], port, servername, WEBHOOK_CONF['webhook_url']))
			else:
				my_logger.warn('{} conf file not found'.format(instance))
	else:
		my_logger.warn('Instances dir not found')
	while True:
		for instance in instances:
			instance.process()
		time.sleep(15)