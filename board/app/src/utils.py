from multiprocessing.connection import wait

import sys
import time
import logging
import os

def get_file(path):
    dir = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(dir, path)

# Function to get the logger for a specific module: do logger = get_module_logger(__name__)
def get_module_logger(mod_name):
    logger = logging.getLogger(mod_name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s [%(name)-12s] %(levelname)-8s %(message)s') # ISO-8601 Format for timestamp
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(os.environ.get('LOG_LEVEL') or 'INFO') # Default to INFO if LOG_LEVEL environment variable is not defined
    return logger

