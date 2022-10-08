from demo.log import log
from demo.greet import message


def hello():
    logger = log.getLogger("the-first-hello-world-logger")

    logger.info("hello world from the first!")
    logger.info(message.get_message())


hello()
