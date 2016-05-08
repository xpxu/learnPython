import conf.conf as xx 
xx.g_filter = True
print xx.g_filter

from conf.conf import g_filter
print g_filter
print xx.g_filter

from client.client_ import run

def main():
    run()

main()
