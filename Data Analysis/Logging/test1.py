from logger import logging
def add(a,b):
    logging.debug("The addition is being done")
    sum=a+b
    print(sum)
    return a+b

logging.debug("The function is called ")
add(10,15)
