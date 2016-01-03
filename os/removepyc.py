from glob import glob
import os,sys

def removepyc():
    filelist =  [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.pyc']
    for i in filelist:
        os.remove(i)


if __name__ == '__main__':
    removepyc()

