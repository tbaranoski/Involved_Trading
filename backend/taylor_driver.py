
from Taylor_package.get_historical_data import Get_Bars
from Config_Alpaca_Clients.config_client import Configure_Client,Configure_Historical_Data_Client
import inspect
import requests
import inspect
import pandas as pd
from Logging_Backend.base_logger import logger
import os
from alpaca.data.live.stock import StockDataStream

from Taylor_package.test_m import getStockData


#Main Program driver for Taylor
#def Taylor_Driver():
    
    # logger.debug("Quant started, Taylor_Driver() started!")    
    
    # ####   GET CLIENT OBJECTS   #####
    # #  Trading Client: For placing trades
    # #  historical_data_client: For fetching historical data   
    # try: 
    #     trading_client = Configure_Client()
    #     historical_data_client = Configure_Historical_Data_Client()
    #     logger.info("Clients configured correctly")
    # except:
    #     logger.error("Trading client/historical data client API Objects NOT configured correctlly") 

    # #Test getting data
    # bars_D = Get_Bars(api = historical_data_client, symbol_or_symbols="TSLA", end = "06/30/2023", start="01/01/2023", timeframe="1Day")
    # #print(bars_D)

    # #print(bars_D.index)

    # #Test Different Timeframes
    # #bars_D = Get_Bars(api = historical_data_client, symbol_or_symbols="TSLA", end = "06/29/2023", start="01/09/2020",timeframe="Day")
    
    # #open = bars_D.loc[:,"symbol"]
    # bars_D.reset_index(inplace = True)

    # print(bars_D.volume.dtypes)
    # #print(type(bars_D.index.get_level_values(0)))
    # #print(type(open.dtypes))
    # print(bars_D)



def Taylor_Driver1():

    logger.debug("Quant started, Taylor_Driver() started!")    
    
    ####   GET CLIENT OBJECTS   #####
    #  Trading Client: For placing trades
    #  historical_data_client: For fetching historical data   
    trading_client = None
    historical_data_client = None

    try: 
        trading_client = Configure_Client()
        historical_data_client = Configure_Historical_Data_Client()
        logger.info("Clients configured correctly")
    except:
        logger.error("Trading client/historical data client API Objects NOT configured correctlly") 

    df = getStockData(symbol='aapl',timeframe='1Month',start= "2023-01-01" , end="2023-07-02", limit= 2000)

    
    print(df)


Taylor_Driver1()


