def thread1():
    for x in range(4):  
        yield  x


def thread2():
    for x in range(4,8):
        yield  x

def thread3():
    for x in range(8,12):
	yield  x

def run(threads):  
    for t in threads:  
        try:  
            print t.next()  
        except StopIteration:  
            pass  
        else:  
            #print 'no exception caught'
            threads.append(t)  

threads=[]
threads.append(thread1())
threads.append(thread2())
threads.append(thread3())
run(threads)
