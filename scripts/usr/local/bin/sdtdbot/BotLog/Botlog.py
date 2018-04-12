'''
Created on 12 avr. 2018

@author: artno
'''
import logging, logging.handlers
from settings import LOG_CONF

def getBotLogger(appName):
    '''
    Create Logger
    '''
    # Set up a specific logger with our desired output level
    my_logger = logging.getLogger(appName)
    my_logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fhandler = logging.handlers.RotatingFileHandler(
        '{}{}.log'.format(LOG_CONF['log_dir'], appName), 
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
    return my_logger