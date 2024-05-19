import sys
import requests
import json
if len(sys.argv)!=2:
    sys.exit('enter value')
# response= requests.get('https://itunes.apple.com/search?entity=song&limit=1&term='+ sys.argv[1])
# print(json.dumps(response.json(), indent=2))
response= requests.get('https://itunes.apple.com/search?entity=song&limit=50&term='+ sys.argv[1]).json()
for result in response['results']:
    print(result['trackId'] , result['trackName'] )