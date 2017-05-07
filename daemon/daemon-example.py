#!/usr/bin/env python

import sys, time
import logging
from daemon import Daemon
import xpapp

class MyDaemon(Daemon):
	def run(self):
		while True:
			time.sleep(10)
			logging.info('--------------------------\n')
			xpapp.myapp()	

if __name__ == "__main__":
	daemon = MyDaemon('/tmp/daemon-example.pid')
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			daemon.start()
		elif 'stop' == sys.argv[1]:
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			daemon.restart()
		else:
			print "Unknown command"
			sys.exit(2)
		sys.exit(0)
	else:
		print "usage: %s start|stop|restart" % sys.argv[0]
		sys.exit(2)
