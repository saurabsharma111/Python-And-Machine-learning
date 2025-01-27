#real life example for logger 
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%d/%m/%Y %I:%M:%S %p',
    handlers=[
        logging.FileHandler('log2.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("Arithmetic app")

def add(a, b):
    try:
        result = a + b
        logger.debug(f"Adding {a} + {b}, result = {result}")
        return result
    except TypeError:
        logger.error("Invalid input type for addition")
        raise ValueError("Invalid input type for addition")

def sub(a, b):
    try:
        result = a - b
        logger.debug(f"Subtracting {b} from {a}, result = {result}")
        return result
    except TypeError:
        logger.error("Invalid input type for subtraction")
        raise ValueError("Invalid input type for subtraction")

def mul(a, b):
    try:
        result = a * b
        logger.debug(f"Multiplying {a} and {b}, result = {result}")
        return result
    except TypeError:
        logger.error("Invalid input type for multiplication")
        raise ValueError("Invalid input type for multiplication")

def div(a, b):
    try:
        if b == 0:
            logger.error("Cannot divide by zero")
            raise ValueError("Cannot divide by zero")
        result = a / b
        logger.debug(f"Dividing {a} by {b}, result = {result}")
        return result
    except TypeError:
        logger.error("Invalid input type for division")
        raise ValueError("Invalid input type for division")
    except ZeroDivisionError:
        logger.error("Cannot divide by zero")
        raise ValueError("Cannot divide by zero")
add(10,20)
sub(10,20)
mul(10,20)
div(10,0)