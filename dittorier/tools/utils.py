__author__ = 'alberto'

import time
from functools import wraps
from dittorier.config import logger


def measure_time(func):
    """
    Decorator that reports the execution time.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logger.info("Execution time: %s", end - start)
        return result

    return wrapper


def chunks(original_list, size):
    """
    Splits a list into smaller lists of size n.
    """
    result = []
    for i in xrange(0, len(original_list), size):
        result.append(original_list[i:i+size])

    return result


def chunks_with_index(original_list, size):
    result = []
    for i in xrange(0, len(original_list), size):
        result.append([i] + original_list[i:i+size])
    return result