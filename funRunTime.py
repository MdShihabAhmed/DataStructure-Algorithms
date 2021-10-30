import time

timeNeeded = float(0)

def timer(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = f(*args, **kwargs)
        
        global timeNeeded
        timeNeeded += time.time()-start
        
        return rv
    return wrapper