from configobj import ConfigObj
config = ConfigObj('config-1.ini')
print config['name']
