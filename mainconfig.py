import configparser
#create object
config=configparser.ConfigParser()
#read file
config.read('config.ini')
#access values
host=config['DATABASE']['host']
user=config['DATABASE']['user']
password=config['DATABASE']['password']
port=config['SETTINGS']['port']
debug=config['SETTINGS']['debug']
print(host,user,password)
print(debug,port)
