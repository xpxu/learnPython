import sys, re
from configobj import ConfigObj
from validate import Validator, ValidateError

email_re = re.compile('\w+@\w+(?:\.\w+)')
def email_check(value):
    if isinstance(value, list):
        raise ValidateError('A list was passed when an email address was expected')
    if email_re.match(value) is None:
        print '"%s" is not an email address' % value
        raise ValidateError('"%s" is not an email address' % value)

    return value


config = ConfigObj('config-email.ini', configspec='configspec-6.ini')

validator = Validator({'email': email_check})
result = config.validate(validator)

'''
if result != True:
    print 'Config file validation failed!'
    sys.exit(1)
else:
    print 'Config file validation succeeded!' 
'''
