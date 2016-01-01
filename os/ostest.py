from glob import glob
import os

def removepyc():
    filelist =  glob('/home/xpxu/tmp_use/test/os/tmp/*.pyc') 
    for i in filelist:
        os.remove(i)


if __name__ == '__main__':
    removepyc()

