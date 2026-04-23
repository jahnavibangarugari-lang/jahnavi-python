import json
with open('config.json','r') as file:
    config=json.load(file)
host=config['database']['host']
port=config['database']['port']
debug=config['settings']['debug']
print(host,port,debug)
