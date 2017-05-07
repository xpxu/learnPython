def singleNumber(a):
    return reduce(lambda x, y: x ^ y, a)

ex = [1, 2, 3, 2, 7]
print singleNumber(ex)