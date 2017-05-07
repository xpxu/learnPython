temp  = '^api-docs/(?P<path>.*)/?$'
pattern = r'%s' % temp

print pattern
print type(pattern)
print type(r'^api-docs/(?P<path>.*)/?$')

name = 'xp'
raise Exception('%s', name)