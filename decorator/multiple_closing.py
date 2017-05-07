'''
Q: what is a decorator?
A: input for a decrator is a function and it will return a new function

'''

def log1(func):
    def wrapper(*args, **kwargs):
        print 'start'
        func(*args, **kwargs)
        print 'end'
    return wrapper


def log2(message):
    # print message
    def decorator(func):
        def wrapper(*args, **kwargs):
            print 'start'
            func(*args, ** kwargs)
            print 'end'
        return wrapper
    return decorator


def log(input):
    if isinstance(input, str):
        # return a decorator
        return log2(input)
    elif hasattr(input, '__call__'):
        # return a function
        return log1(input)
    else:
        raise Exception

# f1 = log(f1)
@log
def f1():
    print '1' * 20

# f2 = log('hello')(f2)
# log('hello') will return a decorator.
@log('hello')
def f2():
    print '2' * 20

f1()
f2()