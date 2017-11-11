import logging

class logData(object):
    def __init__(self):
        fileHandler = logging.FileHandler('RPi_Status.log')
        fileHandler.setFormatter('#Set the format')
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(fileHandler)