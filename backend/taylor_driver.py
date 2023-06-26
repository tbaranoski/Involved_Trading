
from Taylor_package.get_historical_data import Get_D_Bars
from Config_Alpaca_Clients.config_client import Configure_Client,Configure_Historical_Data_Client
import inspect
import requests
import inspect
import pandas as pd
from Logging.base_logger import logger
import os


from alpaca.data.live.stock import StockDataStream


#Main Program driver for Taylor
def Taylor_Driver():
    
    logger.error("debug message log")
    ####   GET CLIENT OBJECTS   #####
    #  Trading Client: For placing trades
    #  historical_data_client: For fetching historical data    
    trading_client = Configure_Client()
    historical_data_client = Configure_Historical_Data_Client()

    #Test getting data
    #def Get_D_Bars(api = None, symbol_or_symbols = None, start= None, end=None, limit=None, timeframe = TimeFrame.Day):

    bars_D = Get_D_Bars(api = historical_data_client, symbol_or_symbols="AAPL")
    print(bars_D)




#Taylor_Driver()

async def update_handler(data):
    print(data)


def test_socket():
    print("start")

    key = os.environ.get('ALPACA_KEY')
    secret_key = os.environ.get('ALPACA_SECRET')
    
    
    
    #Websocket code
    socket_obj = StockDataStream(api_key=key,secret_key=secret_key)
    socket_obj.subscribe_quotes(update_handler, 'AAPL')

    socket_obj.run()

    print("WEBSOCKET STOPPED")

test_socket()
