import logging

class Logger(object):
    """日至记录器"""
    fmt = ("%(asctime)s %(filename)s[line:%(lineno)d]"
           "%(levelname)s - %(message)s")
    datefmt = "%m/%d/%Y %I:%M:%S"

    @classmethod
    def add_handler(cls, handler):
        handler.setLevel(logging.WARNING)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    @staticmethod 
    def config():
        logger = logging.getLogger("{}_log".format(__name__))
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)
        return logger 


if __name__ == "__main__":
    logger = Logger()
