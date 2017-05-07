from configobj import ConfigObj, ConfigObjError
try:
    config = ConfigObj('notexit.file', file_error=True)
except (ConfigObjError, IOError), e:
    print 'Could not read "%s": %s' % ('notexit.file', e)
