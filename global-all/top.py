import conf.conf
from conf.conf import name
from client.client import run

def main():
    conf.g_filter = True
    run()

main()
