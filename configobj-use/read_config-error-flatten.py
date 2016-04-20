from configobj import ConfigObj, flatten_errors
from validate import Validator

config = ConfigObj('config-flatten.ini', configspec='configspec.ini')
validator = Validator()
results = config.validate(validator)

if results != True:
    for (section_list, key, _) in flatten_errors(config, results):
        if key is not None:
            print 'The "%s" key in the section "%s" failed validation' % (key, ', '.join(section_list))
        else:
            print 'The following section was missing:%s ' % ', '.join(section_list)
