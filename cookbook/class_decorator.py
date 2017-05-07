# -*- coding:utf-8 -*-
'''
编写类装饰器
'''

'''
使用全局表来实现单体类装饰器
'''

instances = {}
def getInstance(aClass, *args): # Manage global table
    if aClass not in instances: # Add **kargs for keywords
        instances[aClass] = aClass(*args) # One dict entry per class
    return instances[aClass]

def singleton(aClass): # On @ decoration
    def onCall(*args): # On instance creation
        return getInstance(aClass, *args)
    return onCall


'''
使用封闭作用域来实现单例类装饰器
'''
def singleton(aClass): # On @ decoration
    instance = None # 相当于装饰后的类的一个类属性
    def onCall(*args): # On instance creation
        nonlocal instance # 3.0 and later nonlocal
        if instance == None:
            instance = aClass(*args) # One scope per class
        return instance
    return onCall


'''
使用类来实现单例类装饰器
'''
class singleton:
    def __init__(self, aClass): # On @ decoration
        self.aClass = aClass
        self.instance = None
    def __call__(self, *args): # On instance creation
        if self.instance == None:
            self.instance = self.aClass(*args) # One instance per class
        return self.instance