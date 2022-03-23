"""
Main module of the community board controller
"""
import os
import sys
import time
import traceback
import logging
import pymongo
from utils import get_module_logger
# from rgbmatrix import RGBMatrix, RGBMatrixOptions

# Configure constants
LOGGER = get_module_logger(__name__)
MONGO_USER = os.getenv('MONGO_USER')
MONGO_PASS = os.getenv('MONGO_PASS')
BOARD_DB_NAME = os.getenv('MONGO_DB_NAME')
BOARD_COLLECTION_NAME = 'boardMapping'
MONGO_HOST = os.getenv('MONGO_CONTAINER')
# Create the mongo URI that will be used by the client
MONGO_URI = 'mongodb://'+MONGO_USER+':'+MONGO_PASS+'@'+MONGO_HOST+':27017/?authSource=admin'


def run():
    '''
    The main function of the community board driver,
    initializes the board and launches into the changestream rendering loop
    '''
    LOGGER.info("Beginning Initial Setup")
    mongo_client = pymongo.MongoClient(MONGO_URI)
    board_db = mongo_client[BOARD_DB_NAME]   
    board_collection =   board_db[BOARD_COLLECTION_NAME]

    # TODO: Check for null values on constants
    # Try to connect to the mongodb database
    for _ in range(0,4):
        time.sleep(2)
        try:
            server_info = mongo_client.server_info()
        except pymongo.errors.ServerSelectionTimeoutError as err:
            LOGGER.error(err)
            sys.exit()

        else:
            LOGGER.info('Connected to MongoDB at: %s', MONGO_HOST)
            LOGGER.debug('Database server information: %s', str(server_info))
            break

    # Query for first and last index of collection
    LOGGER.debug('First Entry: %s', str(board_collection.find_one({'index':0})))
    LOGGER.debug('Last Entry: %s', str(board_collection.find_one({'index':2047})))


    LOGGER.info("Beginning Board Rendering Loop")
    while True:
        # TODO: Define interval for rendered updates
        # TODO: Work in MONGODB polling to keep board up to date, maybe look into changestreams
        # TODO: Begin testing in RPI remote docker env
        time.sleep(1)
    return()


if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt as e:
        logging.error(traceback.format_exc())
        sys.exit(e)
