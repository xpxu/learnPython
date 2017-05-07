import logging, sys
#from lib.getname import getname

logging.basicConfig(format=u'%(asctime)s-%(name)s-%(levelname)s: %(message)s', level=logging.DEBUG, stream=sys.stdout)
logger = logging.getLogger('main')

if __name__ == '__main__':
   logger.info('I am main log')
   from lib.getname import getname
   getname()
