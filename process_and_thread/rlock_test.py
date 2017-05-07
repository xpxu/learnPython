import threading
a = 0
b = 0
lock = threading.RLock()
mylock = threading.Lock()

def changeAandB():
    # this function works with an RLock and Lock
    with lock:
        global a, b
        a += 1
        b += 2
        return a, b

def changeAandB2():
    # this function block with Lock
    with mylock:
        print 'start'
        global a, b
        a += 1
        changeAandB2() # block
        b += 2
        print 'end'
        return a, b

def changeAandB3():
    # this function won't block with RLock
    with lock:
        print 'start'
        global a, b
        a += 1
        changeAandB3() # won't block
        b += 2
        print 'end'
        return a, b

print changeAandB()
print changeAandB3() # won't block but will get error with maximum recursion depth exceeded
print changeAandB2() # will  block