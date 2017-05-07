import os

targetdir = os.path.join(os.getcwd(),"tmp")
filelist = os.listdir(targetdir)
for i in filelist:
    oldname = os.path.join(targetdir, i)
    newname = oldname + '.new'
    print oldname 
    print newname
    os.rename(oldname, newname) 

