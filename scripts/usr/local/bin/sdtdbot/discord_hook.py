#!/usr/bin/python3
#-*- coding: utf-8 -*-
'''
Created on 10 avr. 2018

@author: artnod
'''
import os, time, logging, logging.handlers
from lxml import etree
from Webhook.Webhook import Sdtdhook
from settings import WEBHOOK_CONF, SDTD_CONF, LOG_CONF

# Set up a specific logger with our desired output level
my_logger = logging.getLogger('discord_hook')
my_logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fhandler = logging.handlers.RotatingFileHandler(
    '{}discord_hook.log'.format(LOG_CONF['log_dir']), 
    maxBytes = LOG_CONF['max_bytes'], 
    backupCount = LOG_CONF['backup_count']
)
fhandler.setLevel(logging.INFO)
# create console handler with a higher log level
chandler = logging.StreamHandler()
chandler.setLevel(logging.DEBUG)
# create formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
chandler.setFormatter(formatter)
# add the handler to logger
my_logger.addHandler(fhandler)
my_logger.addHandler(chandler)

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