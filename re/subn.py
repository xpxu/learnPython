mystring = "u'zfs_password': u'xenbuild', u'zfs_user': u'root'"

import re

def suppress_keys(context_info, keys):
    '''
    For security reasons, suppress value of keys from the string which
    represent context releted informaition. The key/value is in unicode
    format, like below:

            u'zfs_password': u'xenbuild'

    The targeted keys' valude will be replaced to empty('').
    '''
    for key in keys:
        regex = r"u'%s': u'[^']*'" % key
        newstring = "u'%s': u''" % key
        print regex
        print newstring
        context_info = re.sub(regex, newstring, context_info)
        print context_info 
        #print number
        #print context_info


suppress_keys(mystring, ['zfs_password'])
