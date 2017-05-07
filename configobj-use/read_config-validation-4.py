import sys
from configobj import ConfigObj
from validate import Validator

config = ConfigObj(configspec='configspec-4.ini')

validator = Validator()
result = config.validate(validator)

if result != True:
    print 'Config file validation failed!'
    sys.exit(1)
else:
    print 'Config file validation succeeded!' 
    print config['name']
    print config['attributes']
    print config['favourite_color']
