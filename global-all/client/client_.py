from conf.conf import g_filter
print g_filter

def run():
    if g_filter:
        print 'g_filter is true'
    else:
        print 'g_filter is false'
