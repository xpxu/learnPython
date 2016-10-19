#!/usr/bin/env python
#coding=utf-8
"""
Filename: pool.py
Description: a simple sample for pool class
"""

from multiprocessing import Pool
from time import sleep
import os


def f(x):
    for i in range(10):
        print 'id: %s, %s --- task %s ' % (os.getpid(), i, x)
        sleep(1)


def main():
    pool = Pool(processes=3)    # set the processes max number 3
    for i in range(0,10):
        result = pool.apply_async(f, (i,))
        # result = pool.apply(f, (i,))
    pool.close()
    pool.join()
    if result.successful():
        print 'successful'


if __name__ == "__main__":
    main()
