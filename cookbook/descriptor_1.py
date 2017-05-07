class Descriptor(object):
    def __get__(self, instance, owner):
        pass

class Subject:
    attr = Descriptor()

X = Subject()
X.attr # Roughly runs Descriptor.__get__(Subject.attr, X, Subject)