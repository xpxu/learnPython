def mygen():
    while(True):
        try:
            yield 'something'
        except ValueError:
            yield 'value error'
        finally:
            print 'clean'

gg=mygen()
#print gg.send(2)
print gg.send(None)
print gg.send(1)
print gg.next() #something
print gg.next()
print gg.throw(ValueError) #value error  clean
