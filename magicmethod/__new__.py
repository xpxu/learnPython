class OnlyOne(object):
	_single = None	
	def __new__(cls):
		if cls._single == None:
			cls._single = object.__new__(cls)
		return cls._single

a = OnlyOne()
b = OnlyOne()
assert a == b
