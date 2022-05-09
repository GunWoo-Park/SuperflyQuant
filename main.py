import pprint

import func_arbitrage
import json
import time
import telegram

token = "5149919236:AAGbSkGDR32-9HxzDf6NJ5TpPaXwyEt7geo"

# 5387730578
# 81980522
bot = telegram.Bot(token)
#updates = bot.getUpdates()

#for i in updates:
#    print(i.message)


# Set Variables
#coin_price_url = "https://poloniex.com/public?command=returnTicker"
coin_price_url = "https://api.bybit.com"




"""
    Step 0: Finding coins which can be traded
    Exchange: Bybit
"""
def step_0():

    # Extract list of coins and prices from Exchange
    coin_list = func_arbitrage.get_pybit_tickers(coin_price_url)
    
    # bybit의 경우 생략
    # Loop through each objects and find the tradeable pairs
    #coin_list = func_arbitrage.collect_tradeables(coin_json)

    # Return list of tradeable coins
    return coin_list


""" 
    Step 1: Structuring Triangular Pairs
    Calculation Only
"""
def step_1(coin_list):

    # Structure the list of tradeable triangular arbitrage pairs
    structured_list = func_arbitrage.structure_triangular_pairs(coin_list)

    # Save structured list
    with open("structured_triangular_pairs.json", "w") as fp:
        json.dump(structured_list, fp)


""" 
    Step 2: Calculate Surface Arbitrage Opporunities
    Exchange: Poloniex
    https://docs.poloniex.com/#introduction
"""
def step_2():

    # Get Structured Pairs
    with open("structured_triangular_pairs.json") as json_file:
        structured_pairs = json.load(json_file)

    # Get Latest Surface Prices
    prices_json = func_arbitrage.get_coin_pricepairs(coin_price_url)

    # Loop Through and Structure Price Information
    for t_pair in structured_pairs:
        time.sleep(0.3)

        #pprint.pprint(t_pair)

        prices_dict = func_arbitrage.get_price_for_t_pair(t_pair, prices_json)
        surface_arb = func_arbitrage.calc_triangular_arb_surface_rate(t_pair, prices_dict)

        if len(surface_arb) > 0:
            real_rate_arb = func_arbitrage.get_depth_from_orderbook(surface_arb)
            pprint.pprint(real_rate_arb)
            if real_rate_arb['profit_loss'] > 0:
                bot.sendMessage(chat_id=81980522, text = real_rate_arb)
                bot.sendMessage(chat_id=5387730578, text = real_rate_arb)
            time.sleep(20)

""" MAIN """
if __name__ == "__main__":
    coin_list = step_0()
    structured_pairs = step_1(coin_list)

    #pprint.pprint(coin_list)
    while True:
        step_2()
