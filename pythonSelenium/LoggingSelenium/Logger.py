import logging

class SampleLogger:

    def TestLogger(self):
    # creating the logger
        logger = logging.getLogger(SampleLogger.__name__)
        logger.setLevel(logging.DEBUG)

    # Creating the console handler
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.DEBUG)

    # creating the format

        formatter = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s', datefmt='%d/%m/%Y , %H:%M:%S , %p')

    # Adding formatter to the console handler
        chandler.setFormatter(formatter)

    # adding console handler to the logger
        logger.addHandler(chandler)

    # messages
        logger.debug("This is a debug message")
        logger.info(("This is an information message"))
        logger.warning("This is a warning message")
        logger.error("This is an error message ")
        logger.critical("This is a critical message")

ff = SampleLogger()
ff.TestLogger()

