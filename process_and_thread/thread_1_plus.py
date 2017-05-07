# -*- coding:utf-8 -*-
'''
将myEmail = EmailBackend()定义在全局，此时， myEmail是一个全局变量。
为所有线程所共享。
并且为EmailBackend加一把锁对象。
可以看到，这时候锁起到了作用。
'''

import threading
import time


class EmailBackend(object):
    def __init__(self):
        self._lock = threading.Lock()

    def send_email(self, content):
        with self._lock:
            print content[:5]
            time.sleep(1)
            print content[5:]

# 定义了一个全局变量，该全局变量为所有线程共享
myEmail = EmailBackend()

def mythread(message_content):
    myEmail.send_email(message_content)


t1 = threading.Thread(target= mythread, args=('Alice' * 2,), name='Thread-A')
t2 = threading.Thread(target= mythread, args=('Bobob' * 2,), name='Thread-B')
t3 = threading.Thread(target= mythread, args=('Kevin' * 2,), name='Thread-C')
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()