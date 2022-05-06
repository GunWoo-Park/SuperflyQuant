from pybit import HTTP
import pprint

sym1 = "BTCUSDT"
sym2 = "ETHUSDT"

session = HTTP("https://api-testnet.bybit.com",
               spot=True)
pprint.pprint(session.orderbook(symbol=sym1, limit=20)['result'])
pprint.pprint(session.orderbook(symbol=sym2, limit=20)['result'])