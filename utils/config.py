from configparser import ConfigParser

print("Config read")
config = ConfigParser()
config.read('config.ini')