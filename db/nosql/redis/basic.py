import redis
r = redis.Redis(host='localhost', port = 6379, db=0)
r.set('guo', 'shuai')
print r.get('guo')
print r['guo']
print r.keys()
print r.dbsize()
print r.delete('guo')
r.save()
print r.get('guo') 
r.flushdb()
