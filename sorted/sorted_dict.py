from collections import OrderedDict
import json
import sys
di = {'a':0, 'c':2, 'b':1}
sortedByKey_dic = sorted(di.iteritems(), key = lambda d:d[0], reverse = True)
print sortedByKey_dic
json.dump(OrderedDict(sortedByKey_dic),sys.stdout)
print '\r'

