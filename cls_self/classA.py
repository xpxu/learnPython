class A(object):
    name = 'Lily'
    def foo1(self):
        print "Hello",self
    @staticmethod
    def foo2():
        print "hello"
    @classmethod
    def foo3(cls):
        print "hello"

A.foo2()
print A.name
a = A()
print a.name
a.foo3()
