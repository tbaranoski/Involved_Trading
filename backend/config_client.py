from alpaca.trading.client import TradingClient
import logging
import alpaca
from alpaca.data.historical import StockHistoricalDataClient


#Configuration Files
import config



######################################################################################
######################################################################################
#Configure python CLient (Generic)
def Configure_Client(): 
    try:
        trading_client = TradingClient(config.API_KEY, config.SECRET_KEY)
        return trading_client
    except:
        logging.error("CLIENT FAILED TO CONFIGURE")


def Configure_Historical_Data_Client():
    
    try:
        api = StockHistoricalDataClient(api_key= config.API_KEY, secret_key=config.SECRET_KEY)
        return api
    except:
        logging.error("CLIENT FAILED TO CONFIGURE")
