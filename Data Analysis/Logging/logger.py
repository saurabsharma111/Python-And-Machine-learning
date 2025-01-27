#configure cvustom message
#create a log file names app.log
import logging

logging.basicConfig(
    filename= 'app.log',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%d/%m/%Y %I:%M:%S %p'
)
logging.debug("This is  a debug message")
logging.info("This is info message")
logging.warning("This is a warning")
logging.error("This is a error message")
logging.critical("This is a critical message")