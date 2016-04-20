from configobj import ConfigObj
config = ConfigObj('config-1.ini', encoding='UTF8')
print config['name']
print type(config['name'])
