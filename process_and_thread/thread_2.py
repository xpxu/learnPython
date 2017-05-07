# -*- coding:utf-8 -*-
'''
将myEmail = EmailBackend()在thread内部进行。此时，它变成了一个局部变量.
为每一个线程所私有。
'''

import threading
import time


class EmailBackend(object):
    def __init__(self):
        pass
    def send_email(self, content):
        print content[:5]
        time.sleep(1)
        print content[5:]

# 定义了一个全局变量，该全局变量为所有线程共享
# myEmail = EmailBackend()

def mythread(message_content):
    myEmail = EmailBackend()
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