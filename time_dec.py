import time
from datetime import datetime

cur_time = lambda: datetime.now().microsecond

def time_dec(func):
    def wrapper(*args):
        start_time = cur_time()
        ret = func(*args)
        print(f"{func.__name__} executes in {cur_time() - start_time} ms")
        return ret
    return wrapper


def time_dec_seconds(func):
    def wrapper(*args):
        start_time = time.time()
        ret = func(*args)
        print(f"{func.__name__} executes in {time.time() - start_time}s")
        return ret
    return wrapper
