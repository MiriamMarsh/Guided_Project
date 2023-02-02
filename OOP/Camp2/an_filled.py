#import logging
import os
import sys


#hardcoded folder names:
CURR_DIR = os.path.dirname(__file__)
sys.path.append(CURR_DIR)
LOG_FOLDER =  CURR_DIR + '/logs'
LOG_FILE = LOG_FOLDER + '/camp_logs.txt'
#LOG_FILE = LOG_FOLDER + '/logs.txt'