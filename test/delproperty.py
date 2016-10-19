class people(object):
    income = 1000


b = people()
print b.income
b.name = 'xp'
del b.name
# del b.income
delattr(b, "income")
