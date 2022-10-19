from demo.log import log
from demo.greet import message


def start():
    logger = log.getLogger("the-handler-logger")

    logger.info("Hello World from the handler!")
    logger.info(message.get_message())


start()
