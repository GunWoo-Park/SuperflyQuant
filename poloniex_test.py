import requests
import json

url = "https://poloniex.com/public?command=returnTicker"
req = requests.get(url)
coin_json = json.loads(req.text)


coin_list = []

for coin in coin_json:
    is_frozen = coin_json[coin]["isFrozen"]
    is_post_only = coin_json[coin]["postOnly"]
    if is_frozen == "0" and is_post_only == "0":
        coin_list.append(coin)

print(coin_list)