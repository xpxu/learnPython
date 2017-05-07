#!/usr/bin/env python
# -*- coding: utf-8 -*-
#with_example02.py
 
'''
在with后面的代码块抛出任何异常时，__exit__()方法被执行。
当异常抛出时，与之关联的type，value和trace
传给__exit__()方法，因此抛出的ZeroDivisionError异常被打印出来了。
开发库时，清理资源，关闭文件等等操作，都可以放在__exit__方法当中。

''' 

class Sample:
    def __enter__(self):
        return self
 
    def __exit__(self, type, value, trace):
        print "type is", type
        print "value is", value
        print "trace is", trace
 
    def do_something(self):
        bar = 1/0
        return bar + 10
 
with Sample() as sample:
    sample.do_something()
