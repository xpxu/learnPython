x = {'a':1, 'b': 2} ;
y = {'b':10, 'c': 11}

print (lambda a, b: (lambda a_copy: a_copy.update(b) or a_copy)(a.copy()))(x, y)
