import tarfile
import sys
mytarfile = sys.argv[1]

@profile
def extract_without_clean():
    tar = tarfile.open(mytarfile, 'r')
    #print tar
    for tar_info in tar:
        #print tar_info
        #print '----------------------------'
        #print tar.members
        tar.extract(tar_info)
        #tar.members = []


extract_without_clean()
