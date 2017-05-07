import functools

def info(fun):
    # @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        print 'Kobe',
        fun(*args, **kwargs)
        print 'superstar!'
    return wrapper



@info
def connect1(s1):
    print s1,

@info
def connect2(s1, s2):
    print s1,
    print s2,

@info
def connect3(s1, s2, s3):
    print s1,
    print s2,
    print s3,


print 'connect 1---------------'
connect1('is')
print 'connect 2---------------'
connect2('is', 'a')
print 'connect 3---------------'
connect3('is', 'the', 'only')



