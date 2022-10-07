from components.log import log
from components.greet import message


def hello():
    logger = log.getLogger("the-hello-world-logger")

    logger.info("hello!")
    logger.info(message.get_message())


hello()
