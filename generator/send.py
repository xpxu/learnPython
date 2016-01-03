def consumer():
    r = 'Start'
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    # a None should be send to a generator first. or use c.next().
    r = c.send(None)
    print r
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        # n in (r = c.send(n) ) will be passed to n in (n = yield r)
        # and it start from here,until the next loop to 'yield r',
        # the return value of 'yield r' will be returned to r in
        # (r = c.send(n)). then it stops again.
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
