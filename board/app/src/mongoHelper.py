from multiprocessing.connection import wait

import sys
import time
import logging
import os
import pymongo

# # Sets a single pixel on the board mapping
# def changePixel(db, index, rgbR, rgbG, rgbB):
#     entry = db.boardMapping.findOne({'index' : )
#     result = client.updateOne()
#     return result