class Sample(object):
    def __enter__(self):
        print "In __enter__()"
        return "Foo"
 
    def __exit__(self, type, value, trace):
        print "In __exit__()"
 
 
def get_sample():
    return Sample()
 
 
with get_sample() as sample:
    print "sample is ", sample
