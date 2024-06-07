import logging

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    formatter = logging.Formatter('[%(asctime)s]: %(message)s:')
    ch.setFormatter(formatter)

    logger.addHandler(ch)
    return logger
