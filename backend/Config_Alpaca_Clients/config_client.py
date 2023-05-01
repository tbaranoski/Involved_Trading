from alpaca.trading.client import TradingClient
import logging
import alpaca
from alpaca.data.historical import StockHistoricalDataClient
import os


#Configuration From Enviornemnt Varibales in Windows
key = os.environ.get('ALPACA_KEY')
secret_key = os.environ.get('ALPACA_SECRET')


######################################################################################
#Configure python Client (Generic)
def Configure_Client(): 
    try:
        trading_client = TradingClient(key, secret_key)
        return trading_client
    except:
        logging.error("TRADING CLIENT FAILED TO CONFIGURE")


def Configure_Historical_Data_Client():
    
    try:
        api = StockHistoricalDataClient(key,secret_key)
        return api
    except:
        logging.error("HISTORICAL DATA CLIENT FAILED TO CONFIGURE")
