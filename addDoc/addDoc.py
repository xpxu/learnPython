from abc import ABCMeta

class BaseModel(object):
    __metaclass__ = ABCMeta
    @classmethod
    def get(cls):
        print 'hello, world!'

class User(BaseModel):

    @classmethod
    def get(cls):
        '''
        get docstring
        '''
        super(User, cls).get()
        print 'hello, tmac'

if __name__ == '__main__':
    tmac = User()
    tmac.get() 
    print 'good work'
