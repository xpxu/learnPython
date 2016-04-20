from configobj import ConfigObj
config = ConfigObj('config-3.ini')
print config['Favourites']['food']
software = config['Favourites']['software']
print software['ide']
