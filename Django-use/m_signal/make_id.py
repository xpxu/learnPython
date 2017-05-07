def _make_id(target):
    if hasattr(target, '__func__'):
        return (id(target.__self__), id(target.__func__))
    return id(target)
NONE_ID = _make_id(None)

def mymethod():
    print 'hello'

class myClass():
    def getname(self):
        print 'hello'

my_ID = _make_id(mymethod)
my_Class_ID = _make_id(myClass)
myInstan = myClass()
print dir(myInstan.getname)
my_instance_ID = _make_id(myInstan.getname)

print NONE_ID
print my_ID
print my_Class_ID
print my_instance_ID