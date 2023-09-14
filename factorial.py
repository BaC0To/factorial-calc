import math
import time
import logging
import os

logfile_dir = "C:\\Appl\\BG0VVK_Work\\factorial-calc\\log\\"
logfile_name = "logfile.log"
logfile_path = logfile_dir+logfile_name
if not os.path.exists(logfile_path):
    open(logfile_path, 'w').close()

# create a logger
logging.basicConfig(filename=(logfile_path),filemode="at+",level=logging.DEBUG)
logger = logging.getLogger()


def factorial_calc(n):
    """Function that calculates the factorial value
    param: n: int
    return: result: int"""
    
    try:
        start_time = time.time()
        result = math.factorial(n)
    except (TypeError, ValueError) as exc:
        logger.error(exc)
        raise
    else:
        message = f"The factorial of {n} is {result}"
        print(message)
        logger.info(message)
        return result
    finally:
        end_time = time.time()
        delta_time = abs(end_time - start_time)
        logger.info(f"The computing time is: {delta_time}")


#data = factorial_calc(5)