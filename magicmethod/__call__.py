'''
>>> dir(object)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', 
'__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
'__setattr__', '__sizeof__', '__str__', '__subclasshook__']
'''


class Magicobject(object):

    def __call__(self, *args, **kwargs):
        '''
        dir(object) don't have __call__ atribute, so 
        it's not rewrite here.
        '''
        print '__call__ is called'


if __name__ == '__main__':
    magic = Magicobject()
    magic()
