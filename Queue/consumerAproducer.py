from Queue import Queue

def consumer(q):
    while True:
        r = yield 'whatever'
        print 'get %s from queue' % r
        assert q.get() == r



def producer(q, c):
    for i in range(10):
        q.put(i)
        print 'put %s into queue' % i
        c.send(i)
    print 'Done'


if __name__ == '__main__':
    q = Queue(10)
    c = consumer(q)
    c.send(None)
    producer(q, c)
