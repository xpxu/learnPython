'''
tar file into a buff/fileobj
'''


import tarfile 
from StringIO import StringIO
import os

buff = StringIO()
tarbuff = tarfile.open(fileobj=buff, mode='w')
tarbuff.add('/home/xpxu/study-use/learnPython')
print tarbuff.getmembers()
tarbuff.close()
buff.seek(0, os.SEEK_END)
print buff.tell() 
