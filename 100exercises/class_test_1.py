
class Kls(object):
    no_inst = 0
    def __init__(self):
        Kls.no_inst = Kls.no_inst + 1

    @classmethod
    def get_no_of_instance(cls_obj):
        return cls_obj.no_inst

    def normal_method(self):
        print 'normal'

    @staticmethod
    def static_method():
        print 'static'

ik1 = Kls()
ik2 = Kls()
print Kls.get_no_of_instance()
print ik1.get_no_of_instance()
print Kls.get_no_of_instance()
print ik1.no_inst
print ik2.no_inst
print Kls.no_inst
# print Kls.normal_method()
Kls.static_method()


