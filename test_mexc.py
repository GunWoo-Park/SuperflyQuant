import requests
import json
import pprint

url = "https://www.mexc.com/open/api/v2/market/api_default_symbols"
#url = "https://contract.mexc.com/api/v1/contract/risk_reverse/history?symbol=BTC_USDT&page_num=1&page_size=20"
#headers = {
#  'Accept': 'application/json'
#}



resp = requests.get(url)

#r = response.json()

pprint.pprint(resp)

#response.
#json_resp = json.loads(r)

#pprint.pprint(json_resp)



#print(r.json())
