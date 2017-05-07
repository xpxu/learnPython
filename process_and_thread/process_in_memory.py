# -*- coding:utf-8 -*-

# 代码段，存放在.text, 在内存中是只读的
# 代码段是进程和线程共享的。
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

# 定义一个全局变量，存放在.data， 在内存中可读写
# .data段是进程和线程共享的。
global_stuent = Student('xp')

# 代码段，存放在.text，
def getname():
    # 定义一个局部变量, 该变量存放在内存的栈当中，由线程私有
    local_stuent = Student('wxy')
    print local_stuent
    print global_stuent


getname()

