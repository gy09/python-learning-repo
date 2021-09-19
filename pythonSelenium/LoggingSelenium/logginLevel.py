import logging

logging.basicConfig(filename='Test.log', filemode='a', format='%(asctime)s: %(levelname)s: %(message)s',
                    level=logging.ERROR, datefmt="%d/%m/%Y %H:%M:%S %p")

logging.debug("This is a Debug message")
logging.info("This is an Information Message")
logging.warning("This is a warning Message")
logging.error("This is an error message")
logging.critical("This is a critical message")
