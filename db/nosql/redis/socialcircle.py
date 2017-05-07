# -*- coding: utf-8 -*-

import redis
r = redis.Redis(host='localhost', port = 6379, db=0)
r.sadd('circle:game:lol','user:debugo')
r.sadd('circle:game:lol','user:leo')
r.sadd('circle:game:lol','user:Guo')
r.sadd('circle:soccer:InterMilan','user:Guo')
r.sadd('circle:soccer:InterMilan','user:Levis')
r.sadd('circle:soccer:InterMilan','user:leo')

#获得某一圈子的成员
print r.smembers('circle:game:lol')

# 求差集
print r.sinter('circle:game:lol', 'circle:soccer:InterMilan')

# 求并集
for i in  r.sunion('circle:game:lol', 'circle:soccer:InterMilan'):
    print i

