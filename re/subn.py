mystring = "u'zfs_password': u'xenbuild', u'zfs_user': u'root'"

import re

def suppress_keys(context_info, keys):
    '''
    For security reasons, hide values of keys from the string which
    represents context related informaition. The key/value is in unicode
    format, likes below:

            u'zfs_password': u'xenbuild'

    The targeted key's value will be replaced to empty('').
    '''
    for key in keys:
        regex = r"u'%s': u'[^']*'" % key
        newstring = "u'%s': u''" % key
        context_info = re.sub(regex, newstring, context_info)
    return context_info


result = suppress_keys(mystring, ['zfs_user'])
print result
