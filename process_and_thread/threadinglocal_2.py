# -*- coding:utf-8 -*-
'''
This test will compare a threadinglocal varibale
with a regular variable.
'''

import threading, time

# .text
class ThreadStudent(threading.local):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

# .data
t_student = ThreadStudent('xp')

# .text
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
# .data
student = Student('wxy')

# .text
def mythread_1(name):
    '''
    This method will read/write t_student
    '''
    t_student.name = name
    time.sleep(1)
    print 'mythread_1:%s:%s' % (threading.current_thread().name, t_student)

# text
def mythread_2(name):
    student.name = name
    time.sleep(1)
    print 'mythread_2:%s:%s' % (threading.current_thread().name, student)

# text
# thread-A should be Alice and thread-B should be Bob.
t1 = threading.Thread(target= mythread_1, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= mythread_1, args=('Bob',), name='Thread-B')
t3 = threading.Thread(target= mythread_2, args=('Alice',), name='Thread-A')
t4 = threading.Thread(target= mythread_2, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()

# result:
# mythread_1:Thread-A:Alice
# mythread_1:Thread-B:Bob
# mythread_2:Thread-A:Bob
# mythread_2:Thread-B:Bob




