import conf.conf

def run():
    if conf.g_filter:
        print 'good'
    else:
        print 'bad'
