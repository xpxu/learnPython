import crash_on_ipy

def fun1(*args, **kwargs):
    for i in range(10):
        print i
        if i == 8:
            raise KeyError(i)


print 'It is a test'
fun1()
