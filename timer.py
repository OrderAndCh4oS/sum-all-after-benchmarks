import time


def timer(f, param):
    start = time.time()
    r = False
    for i in range(1000):
        r = f(param)
        if isinstance(r, int) and r == -1:
            return -1

    return (time.time() - start) / 1000 if r is not False else -1
