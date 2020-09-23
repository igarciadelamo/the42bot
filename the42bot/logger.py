import logging


class Bot42Logger:

    @staticmethod
    def getLogger(filename):
        logger = logging.getLogger("the42bot")
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        handler = logging.FileHandler(filename)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        return logger