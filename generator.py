

import os
import json
import requests

data = requests.get('http://192.168.100.212:3000/swagger')
with open('api.json', 'w') as file:
    json.dump(json.loads(data.content), file)

os.system('openapi-generator-cli generate -g dart  -i api.json -o api')
os.system('flutter pub get api')