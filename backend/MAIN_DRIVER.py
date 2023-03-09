from alpaca.trading.client import TradingClient
import logging



import config


###   Configure Logger   ###

#Set log level to INFO to debug (WARNING is default)
logging.basicConfig(level=logging.WARNING)

##########################################################################################################
##########################################################################################################
##########################################################################################################
def Configure_Client():
    
    try:
        trading_client = TradingClient(config.API_KEY, config.SECRET_KEY)
        return trading_client
    except:
        logging.error("CLIENT FAILED TO CONFIGURE")


def main():
    alpaca_obj = Configure_Client()

##########################################################################################################
##########################################################################################################
##########################################################################################################
main()