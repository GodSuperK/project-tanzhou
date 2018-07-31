import logging


class Logger(object):
    """日志记录器"""
    fmt = ("%(asctime)s %(filename)s[line:%(lineno)d]"
           "%(levelname)s - %(message)s")

    fmt2 = ("\033[0;34m%(asctime)s\033[0m"
            " \033[0;31m%(levelname)s\033[0m"
            " [\033[0;32mline:%(lineno)d\033[0m %(message)s]")

    datefmt = "%Y-%m-%d %I:%M:%S"

    formatter = None

    @classmethod
    def add_handler(cls, logger, handler):
        """将Handler 实例加入到 Logger中"""
        handler.setLevel(logging.WARNING)
        handler.setFormatter(cls.formatter)
        logger.addHandler(handler)

    @classmethod
    def get_logger(cls):
        """返回一个日志记录器"""
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        cls.formatter = logging.Formatter(fmt=cls.fmt2, datefmt=cls.datefmt)
        return logger


def logger_init():
    logger = Logger.get_logger()

    console_handler = logging.StreamHandler()
    file_logging_handler = logging.FileHandler("program.log")

    Logger.add_handler(logger, console_handler)
    Logger.add_handler(logger, file_logging_handler)

    return logger


def main():
    logger = logger_init()
    try:
        import xxx
    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    main()
