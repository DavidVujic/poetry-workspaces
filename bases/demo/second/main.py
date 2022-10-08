from demo.log import log
from demo.greet import message


def second_hello():
    logger = log.getLogger("the-second-hello-world-logger")

    logger.info("Hello from the second!")
    logger.info(message.get_message())


second_hello()
