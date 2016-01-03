'''
>>> dir(object)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', 
'__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
'__setattr__', '__sizeof__', '__str__', '__subclasshook__']
'''
class Magicobject(object):

    def __init__(self, name, age):
        self.name = self.name
        self.age = self.age

    def __getattr__(self, item):
        if item == 'name':
            return 'Kobe'
        elif item == 'age':
            return 26

class Player(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == '__main__':

    tmac = Player('Tmac', '18')
    print tmac.name
    print tmac.age

    tmac = Magicobject('Tmac', '18')
    print tmac.name
    print tmac.age

