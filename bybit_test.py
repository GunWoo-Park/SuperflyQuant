import pprint
import json

from pybit import HTTP
session = HTTP(
    endpoint="https://api.bybit.com",
    spot=True
)

symbols = session.query_symbol()

result = symbols['result']

names = []

for symbol in result:
    names.append(symbol['name'])

resp = []
strnum = []

i = 0

for name in names:
     resp.append(name)
     num = resp[i].find('USDT')
     if num == -1:
        num = resp[i].find('DAI')
     if num == -1:
        num = resp[i].find('UST')
     if num == -1:
        num = resp[i].find('BTC')
     if num == -1:
        num = resp[i].find('USDC')

     resp[i] = resp[i][0:num] + '_' + resp[i][num:]

     i = i + 1

with open("structured_triangular_pairs.json") as json_file:
    structured_pairs = json.load(json_file)

pprint.pprint(structured_pairs)



