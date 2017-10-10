from time import time

def timer(func):
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print 'elapsed time', after-before
        return rv
    return f

def twice(func):
    def wrapper(*args, **kwargs):
        for _ in range(2):
            print 'running {.__name__}'.format(func)
            rv = func(*args, **kwargs)
        return rv
    return wrapper

@twice
def add(x, y):
    return x + y

@twice
def sub(x, y):
    return x-y

print 'add->', add(10, 20)
print 'sub->', sub(100, 30)
