from simplesignal import Signal
import threading

mysignal = Signal(providing_args=['hobby'])


def callback(sender, **kwargs):
    print "%s:%s" %(threading.current_thread().name, kwargs['hobby'])

def mytask(*args):
    mysignal.connect(callback, sender=args[0])
    mysignal.send(args[0], hobby=args[1])

t1 = threading.Thread(target=mytask, args=('Alice','banana',), name='Thread-A')
t2 = threading.Thread(target=mytask, args=('Kevin', 'apple',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
