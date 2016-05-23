import tarfile
import sys
mytarfile = sys.argv[1]

@profile
def extract_all():
    tar = tarfile.open(mytarfile, 'r')
    #print tar
        #print tar_info
        #print '----------------------------'
        #print tar.members
    tar.extractall()
        #tar.members = []


extract_all()
