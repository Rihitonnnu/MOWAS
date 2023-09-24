import logging


class Log:
    def __init__(self, filename):
        self.filename = filename

    def setup(self):
        logging.basicConfig(filename=self.filename, encoding='utf-8',
                            format='%(asctime)s %(message)s', level=logging.DEBUG,)
        logger = logging.getLogger(__name__)
        return logger
