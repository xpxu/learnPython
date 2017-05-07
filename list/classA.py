class A(object):
    def foo1(self):
        print "Hello",self
    @staticmethod
    def foo2():
        print "hello"
    @classmethod
    def foo3(cls):
        print "hello",cls


A.foo3()
