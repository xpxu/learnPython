import os
print __file__
filepath = os.path.abspath(__file__)
print os.path.dirname(filepath)
print os.path.dirname(os.path.dirname(filepath))
