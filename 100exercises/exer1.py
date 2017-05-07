
ret = []
ret = [str(x) for x in xrange(2000, 3201) if x % 7 == 0 and x % 5 != 0]
print ','.join(ret)