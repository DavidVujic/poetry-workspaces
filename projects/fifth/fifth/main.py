from demo.log import log

logger = log.getLogger("THIS IS THE FIFTH")


def hello():
    logger.info("HELLO WORLD")
