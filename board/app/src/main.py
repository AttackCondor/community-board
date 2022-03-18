from multiprocessing.connection import wait

import sys
import time
import traceback
import pymongo
import logging
from utils import get_module_logger
# from rgbmatrix import RGBMatrix, RGBMatrixOptions

# Configure logging constant
LOGGER = get_module_logger(__name__)

def run():
    LOGGER.info("Beginning Board Rendering Loop")
    while True:
        # TODO: Define interval for rendered updates
        # TODO: Interface with MOGODB
        # TODO: Work in MONGODB polling to keep board up to date, maybe look into changestreams
        # TODO: Begin testing in RPI remote docker env
        time.sleep(1)


if __name__ == '__main__':
    try:
        run()
    except Exception as e:
        logging.error(traceback.format_exc())
        sys.exit(e)