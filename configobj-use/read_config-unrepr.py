from configobj import ConfigObj
config = ConfigObj('config-4.ini', unrepr=True)
print config['kid.encoding']
print config['tg.allow_json']
print config['tg.mapping']
