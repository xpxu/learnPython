import re

s1 = 'api-docs/user' 
s2 = 'api-docs/user/anything'
s3 = 'api-docs/user/'
temp  = '^api-docs/(?P<path>.*)/?$'
pattern = r'%s' % temp
pattern = r'^api-docs/(?P<path>.*)/?$'
print 'test1 is %s' % re.findall(pattern, s1)
print 'test2 is %s' % re.findall(pattern, s2)
print 'test3 is %s' % re.findall(pattern, s3)
