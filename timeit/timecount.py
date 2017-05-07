from timeit import Timer
import functools

def timecount(fun):
    @functools.wraps(fun)
    def wrapper():
        #t = Timer('fun','from __main__ import fun')
        #t = Timer('fun','from __main__ import fun.__name__')
        #funname = fun.__name__ 
        #print 'funname is %s' % funname
        stmt = '%s' % fun.__name__
        setup = 'from __main__ import %s' % fun.__name__
        print 'stmt is %s, setup is %s' % (stmt, setup)
        print 'stmt is {0}, setup is {1}'.format(stmt, setup)
        t = Timer(stmt, setup)
        return t.timeit()
    return wrapper


@timecount
def _fun():
    def f(x):
        return x*x
    return map(f, [1, 2, 3])


print '_fun time is %s' % _fun()

