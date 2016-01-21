#/usr/bin/python  
import os  
import sys
  
#count the line of a single file  
def CountLine(path):  
        tempfile = open(path)  
        res = 0  
        for lines in tempfile:  
                res += 1  
        print "%s %d" %(path, res) #output the file path and lines  
        tempfile.close()  
        return res  
  
#count the total line of a folder, sub folder included  
def TotalLine(path):  
        total = 0  
        for root, dirs, files in os.walk(path):  
                for item in files:  
                        ext = item.split('.')  
                        ext = ext[-1]  #get the postfix of the file  
                        if(ext in ["py"]):  
                                subpath = root + "/" + item  
                                total += CountLine(subpath)  
        return total  
  
path = sys.argv[1]
print "Input Path is %s" % path  
print TotalLine(path)
