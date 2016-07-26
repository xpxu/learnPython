xp_d = {'_CreateConfig__ilom_password': u'ADMIN000', u'zfs_servers': [{u'zfs_password': u'xenbuild', u'zfs_user': u'root', u'zfs_size': u'25G', u'zfs_be_server': u'10.128.94.120', u'zfs_pool': u'virtclust-0', u'zfs_server': u'10.128.94.120', u'zfs_interface': u'zif'}], '_CreateConfig__control_plane_iloms': [u'scan05cn02-c.us.oracle.com', u'scan05cn03-c.us.oracle.com', u'scan05cn04-c.us.oracle.com'], '_CreateConfig__config_prod_options': {u'post_config_json': {u'appid_pass': u'welcome1', u'domain': u'us.oracle.com'}}}


class MyDict(object):
    def __init__(self):
        self.__configuration = xp_d

def suppress_keys(d, hidden):
    output = {}
    for key, value in d.items():
        if key in hidden:
            output[key] = '***'
        elif isinstance(value, dict):
            output[key] = suppress_keys(value, hidden)
        elif isinstance(value, list):
            suppressed_value = []
            for i in value:
               if isinstance(i, dict):
                   suppressed_value.append(suppress_keys(i, hidden))
               else:
                   suppressed_value = value
                   break
            output[key] = suppressed_value
        else:
            output[key] = value
    return output


# infile = open('config')
# my_d = dict(infile.read())
# infile.close()
my_d = MyDict()
print type(my_d.__dict__)
print my_d.__dict__
result = suppress_keys(my_d.__dict__,[u'zfs_password'])
#outfile = open('result','w')
#outfile.write(result)
#outfile.close()
print result
