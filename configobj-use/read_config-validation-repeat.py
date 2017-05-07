import sys
from configobj import ConfigObj
from validate import Validator

config = ConfigObj('config-repeat.ini', configspec='configspec-5.ini')

validator = Validator()
result = config.validate(validator)

if result != True:
    print 'Config file validation failed!'
    sys.exit(1)
else:
    print 'Config file validation succeeded!' 
