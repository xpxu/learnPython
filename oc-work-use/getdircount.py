import os

dircount = 1
for root, dirs, files in os.walk('src'):
    print root
    print dirs
    print files
    dircount += len(dirs)
    dircount += len(files)


print dircount
