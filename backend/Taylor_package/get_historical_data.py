from datetime import datetime, date, timedelta
from typing import Dict
import pandas as pd
from typing import Union
from Taylor_package.format_datetime import Format_Datetime, Format_Timeframe_String

#Imports copioed from example
from alpaca.data import Trade, Snapshot, Quote, Bar
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import (
    StockBarsRequest,
    StockQuotesRequest,
    StockTradesRequest,
    StockLatestTradeRequest,
    StockLatestQuoteRequest,
    StockSnapshotRequest,
    StockLatestBarRequest,
)
from alpaca.data.timeframe import TimeFrame
from alpaca.data.enums import Exchange, DataFeed
from alpaca.data.models import BarSet, QuoteSet, TradeSet

from alpaca.data.timeframe import TimeFrame
from Logging_Backend.base_logger import logger



#Returns Dataframe of Data for ticker
def Get_Bars(api = None, symbol_or_symbols = None, start= None, end=None, limit=None, timeframe = "1Day"):

    barset_returned = None
    time_param_arr = None     
    time_frame_obj = None
    time_frame_string_code = None 

    #Format start and end dates
    try:        
        
        #Construction Start
        #Get Timeframe object for request and timeframe string code (to know what to remap data too)
        arr = Format_Timeframe_String(timeframe = timeframe)
        time_frame_obj = arr[0]  
        time_frame_string_code = arr[1]  

        #Get object-formatted start and end dates/times
        time_param_arr = Format_Datetime(start_date = start, end_date = end , time_frame=time_frame_string_code, limit= limit)

        logger.debug("Start and Endate objects for get_bars configured Successfully")        
        logger.debug("Start Date: %s",str(time_param_arr[0]))        
        logger.debug("End Date: %s",str(time_param_arr[1]))
        
    except:
        logger.error("Error formatting start and endtime datetime objects")

    #Formulate request to Alpaca Historical CLient
    try:
        request = StockBarsRequest(symbol_or_symbols = symbol_or_symbols, timeframe= time_frame_obj, start= time_param_arr[0], end=time_param_arr[1])        
        barset_returned = api.get_stock_bars(request_params=request).df
        logger.info("Barset request succesfull")
    except:
        logger.error("Error formatting/requesting barset from Alpaca")

    #Return dataframe
    return barset_returned


