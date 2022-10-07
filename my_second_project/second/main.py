from components.log import log
from components.greet import message


def second_hello():
    logger = log.getLogger("the-second-hello-world-logger")

    logger.info("Hello from the second project!")
    logger.info(message.get_message())


second_hello()
