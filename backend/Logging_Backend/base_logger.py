import logging
from datetime import datetime
import os


#CONSTANTS
#EX: LOG_FOLDER_PATH = 'LOGS/'
#LOGGING LEVELS: 
# CRITICAL
# ERROR
# WARNING
# INFO
# DEBUG
LOG_FOLDER_PATH = 'LOGS/' #PATH WITHIN INVOLVED_TRADING DIRECTORY
LOG_LEVEL = logging.DEBUG
#######################################################




#Current Date/Time dd/mm/YY H:M:S
now = datetime.now()

#Create File name
dt_string_now = now.strftime("%d-%m-%Y   %I-%M-%S %p")
file_name = dt_string_now + '.log'

#Initialize global logger for backend with file for every run
logger = logging
logger.basicConfig(level = LOG_LEVEL,filename=LOG_FOLDER_PATH+file_name, format='%(asctime)s %(levelname)s    %(message)s         %(pathname)s',filemode='w')