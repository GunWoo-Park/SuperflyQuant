import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.delta.exchange/v2/products', params={

}, headers = headers)

print(r.json())