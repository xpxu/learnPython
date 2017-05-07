#from conf.conf import g_filter
import conf.conf

def run():
    if conf.g_filter:
        print 'g_filter is true'
    else:
        print 'g_filter is false'
