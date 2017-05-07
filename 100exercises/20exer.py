
def putNumbers(n):
    return (x for x in range(0, n, 7))


for x in putNumbers(100):
    print x