def tag_wrap(tag):
    def whatever(fn):
        def inner(s):
            return '<%s>%s' % (fn(s), tag)
        return inner
    return whatever 
 
@tag_wrap('b')
@tag_wrap('em')
def greet(name):
    return 'Hello, %s!' % name
 
print(greet('world'))
