s = set([1, 1, 2, 2, 3, 3])
s.add(4)
s.add(4)
print s
s.remove(4)
print s

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print s1 & s2
print s1 | s2

