#!/usr/bin/python

import logging
import sys

#logging.basicConfig(format=u'%(asctime)s %(levelname)s: %(message)s', level=logging.ERROR, stream=sys.stdout)
logger = logging.getLogger('simple-test')
logger.setLevel(logging.DEBUG)  


if __name__ == '__main__':
    logger.info('hello, info')
    logger.debug('helo, debug')
