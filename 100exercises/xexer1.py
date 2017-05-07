
def s1():
    for i in range(1, 5):
        output = [str(i) + " " + str(x) for x in range(1, 5)]
        print '\n'.join(output)
        print ''

def s2():
    for m in range(1,5):
        for n in range(1,m+1):
            print m," ",n
        print "\n",

s2()