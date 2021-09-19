from LoggingSelenium.customLogger import customlogger
import logging


class Test_Method():

    log = customlogger(logging.DEBUG())

    def method_1(self):
        self.log.debug("This is a Debug message")
        self.log.info("This is an Information Message")
        self.log.warning("This is a warning Message")
        self.log.error("This is an error message")
        self.log.critical("This is a critical message")

    def method_2(self):

        metlog = customlogger(logging.INFO())

        metlog.debug("This is a Debug message")
        metlog.info("This is an Information Message")
        metlog.warning("This is a warning Message")
        metlog.error("This is an error message")
        metlog.critical("This is a critical message")


demo = Test_Method()
demo.method_1()
demo.method_2()
