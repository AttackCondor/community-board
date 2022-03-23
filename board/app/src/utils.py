'''Utils module for supplemetal functions'''
import logging
import os

def get_file(path):
    ''' Get a specific file using the path'''
    directory = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(directory, path)

# Function to get the logger for a specific module: do logger = get_module_logger(__name__)
def get_module_logger(mod_name):
    ''' Gets an appropriate logger to handle the module'''
    logger = logging.getLogger(mod_name)
    handler = logging.StreamHandler()
    # ISO-8601 Format for timestamp
    formatter = logging.Formatter('%(asctime)s [%(name)-12s] %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    # Default to INFO if LOG_LEVEL environment variable is not defined
    logger.setLevel(os.environ.get('LOG_LEVEL') or 'INFO')
    return logger
