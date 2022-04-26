import requests
from requests.auth import HTTPBasicAuth

url = 'https://betsson-en--coe.custhelp.com/services/rest/connect/v1.4/contacts'
payload = {
  "name": {
    "first": "Jonathan",
    "last": "Randall"
  }
}
headers =  {"OSvC-CREST-Application-Context":"test"}
iteratorCount = 890
while iteratorCount != 0:
    response = requests.post(url, json=payload, auth = HTTPBasicAuth('OracleTestAgent', 'Oracle@123'), headers = headers)
    print(response)
    iteratorCount = iteratorCount - 1
    