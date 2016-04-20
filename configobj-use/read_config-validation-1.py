import sys
from configobj import ConfigObj
from validate import Validator

config = ConfigObj('config-1.ini', configspec='configspec-1.ini')

validator = Validator()
result = config.validate(validator)

if result != True:
    print 'Config file validation failed!'
    sys.exit(1)
else:
    print 'Config file validation succeeded!' 
