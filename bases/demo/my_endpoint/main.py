from demo.log import log
from demo.greet import message


def start():
    logger = log.getLogger("the-endpoint-logger")

    logger.info("Hello World from the endpoint!")
    logger.info(message.get_message())


start()
