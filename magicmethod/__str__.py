class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return "%s" % self.name

    def __repr__(self):
        return self.__str__()

def getstudentage(x):
	print x.age

def getname(*arg):
    print type(*arg)
    print type(arg)
    print arg
    # pass *arg as object
    getstudentage(*arg)

# s is an object
s = Student('xp', '18', '100')
# pass s as a string 
getname(s)
