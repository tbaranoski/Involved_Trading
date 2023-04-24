from alpaca.trading.client import TradingClient
import logging
from alpaca.data.historical import StockHistoricalDataClient
import alpaca
import get_historical_data

#Configuration Files
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


#Test for pulling bar data from client
def Get_Stock_Data(client):
    historical_data_client = StockHistoricalDataClient(client)
    historical_data_client.get_stock_bars()

def main():
    api = Configure_Client()
    get_historical_data.Get_D_Bars(api)

#test commit 
def test():
    print("test")
    # sup
##########################################################################################################
##########################################################################################################
##########################################################################################################
main()



#test commit taylor