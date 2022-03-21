from multiprocessing.connection import wait

import os
import sys
import time
import traceback
import pymongo
import logging
from utils import get_module_logger
# from rgbmatrix import RGBMatrix, RGBMatrixOptions

# Configure constants
LOGGER = get_module_logger(__name__)
MONGO_USER = os.getenv('MONGO_USER')
MONGO_PASS = os.getenv('MONGO_PASS')
BOARD_DB_NAME = os.getenv('MONGO_DB_NAME')
BOARD_COLLECTION_NAME = 'boardMapping'
MONGO_HOST = os.getenv('MONGO_CONTAINER')
MONGO_URI = 'mongodb://' + MONGO_USER + ':' + MONGO_PASS + '@' + MONGO_HOST + ':27017/?authSource=admin' # Create the mongo URI that will be used by the client




def run():

    LOGGER.info("Beginning Initial Setup")
    mongoClient = pymongo.MongoClient(MONGO_URI)
    boardDb = mongoClient[BOARD_DB_NAME]
    boardCollection = boardDb[BOARD_COLLECTION_NAME]

    # TODO: Check for null values on constants
    # Try to connect to the mongodb database
    for x in range(0,4):
        time.sleep(2)
        try:
            serverInfo = mongoClient.server_info()
        except pymongo.errors.ServerSelectionTimoutError as err:
            LOGGER.error(err)
            sys.exit()

        else:
            LOGGER.info('Connected to MongoDB at: ' + MONGO_HOST)
            LOGGER.debug('Database server information:  ' + str(serverInfo))
            break
    
    # Query for first and last index of collection
    LOGGER.debug('First Entry:' + str(boardCollection.find_one({'index':0})))
    LOGGER.debug('Last Entry: ' + str(boardCollection.find_one({'index':2047})))


    LOGGER.info("Beginning Board Rendering Loop")
    while True:
        # TODO: Define interval for rendered updates
        # TODO: Work in MONGODB polling to keep board up to date, maybe look into changestreams
        # TODO: Begin testing in RPI remote docker env
        time.sleep(1)


if __name__ == '__main__':
    try:
        run()
    except Exception as e:
        logging.error(traceback.format_exc())
        sys.exit(e)