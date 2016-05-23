# -*- coding:utf-8 -*-
# metaclass是创建类，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
	'''
	__new__()方法接收到的参数依次是：

	当前准备创建的类的对象；

	类的名字；

	类继承的父类集合；

	类的方法集合。
	'''
        print '__new__ is called'
        print 'cls is %s' % cls
        print 'name is %s' % name
        print 'bases is %s' % bases
        print 'origin attrs is %s' % attrs
        attrs['add'] = lambda self, value: self.append(value)
        print '-------------------'
        print 'changed attrs is %s' % attrs 
        return type.__new__(cls, name, bases, attrs)

class MyList(list):
    __metaclass__ = ListMetaclass # 指示使用ListMetaclass来定制类


if __name__ == '__main__':
    L = MyList()
    L.add(1)
    print L
