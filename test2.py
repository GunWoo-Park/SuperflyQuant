from BybitWebsocket import BybitWebsocket
import logging
from time import sleep

def setup_logger():
    # Prints logger info to terminal
    logger = logging.getLogger()
    logger.setLevel(logging.INFO) # Change this to DEBUG if you want a lot more info
    ch = logging.StreamHandler()
    # create formatter
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger

if __name__ == "__main__":
    logger = setup_logger()
    # inverse perpetual
    ws = BybitWebsocket(wsURL="wss://stream.bybit.com/spot/quote/ws/v2",
                        api_key="", api_secret="" 
                        ) 
    ws.subscribe_orderBookL2("BTCUSDT")

    while(1):
        logger.info(ws.get_data("orderBookL2_25.BTCUSDT"))
        sleep(1)
