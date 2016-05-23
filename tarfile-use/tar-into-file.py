'''
tar into a file
'''


import tarfile 
import os

tar = tarfile.open('metaclass.tar', mode='w')
tar.add('metaclass')
tar.close()
