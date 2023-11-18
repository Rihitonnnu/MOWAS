import logging


def log_instance(file):
    logger = logging.getLogger(file)
    logger.setLevel(10)
    sh = logging.StreamHandler()
    logger.addHandler(sh)
    fh = logging.FileHandler('../log/{}.log'.format(file),
                             encoding='utf-8', mode='w')
    logger.addHandler(fh)
    formatter = logging.Formatter('%(message)s')
    fh.setFormatter(formatter)
    sh.setFormatter(formatter)
    return logger
