import json
from collections import OrderedDict

with open('occ_whitelist_api_swagger.json', 'r') as f:
    description_info = json.loads(f.read())


description_info['tags'].sort()
description_list = [(k,v) for k, v in description_info['definitions'].iteritems()]
description_list.sort()
description_info['definitions'] = OrderedDict(description_list)

with open('new_occ_all_api_swagger.json', 'w') as f:
   json.dump(OrderedDict(description_info), f, indent = 4)
