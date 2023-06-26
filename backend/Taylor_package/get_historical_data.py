from datetime import datetime
from typing import Dict
import pandas as pd
from typing import Union

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
from datetime import datetime, date, timedelta
from Logging.base_logger import logger

#Constants
DAY_LIMIT_DEFAULT = 365




#Format datetime into datetime objects
def Format_Datetime(start_date, end_date, time_frame, limit = None):

    todays_date = date.today()
    end_datetime_obj = None
    start_datetime_obj = None

    today_date_year = todays_date.strftime("%Y")
    today_date_month = todays_date.strftime("%m")
    today_date_day = todays_date.strftime("%d")

    #####   END DATES FORMAT   #####
    #If no end date passed in, today is end date
    if(end_date == None):
        yo = datetime(today_date_year, today_date_month, today_date_day)

    #If end_date was given in correct datetime object format, pass through function
    elif((type(end_date)) == type(datetime(2022,1,1))):
        end_datetime_obj = end_date

    #A string was passed in, reformat
    #Format passed in 07/01/2023
    elif(isinstance(end_date,str)):
        date_array = end_date.split('/')
        end_datetime_obj = datetime(date_array[2], date_array[1], date_array[0])


    #####   START DATES FORMAT   #####
    #If no Start Date passed in choose one based on limit. If NO limit is passed, default to set amount
    if(start_date == None):

        #If a limit is given find start date
        if(limit != None):
            start_datetime_obj = (datetime(today_date_year, today_date_month, today_date_day) - (timedelta(days=limit)))

        #No limit given, use default
        else:
            start_datetime_obj = (datetime(today_date_year, today_date_month, today_date_day) - (timedelta(days=DAY_LIMIT_DEFAULT)))

    #If start_date was given in correct datetime object format, pass through function
    elif((type(start_date)) == type(datetime(2022,1,1))):
        start_datetime_obj = start_date

    #A string was passed in, reformat
    #Format passed in 07/01/2023
    elif(isinstance(start_date,str)):
        date_array = end_date.split('/')
        start_datetime_obj = datetime(date_array[2], date_array[1], date_array[0])

    ###############################################################################
    ###   ERROR CHECK (Make sure start date is before end date)   ###
    if(start_datetime_obj >= end_datetime_obj):
        logger.error("Start Date and End Date Reversed")


    return [start_date,end_date]


#Returns Dataframe of Data for ticker
def Get_D_Bars(api = None, symbol_or_symbols = None, start= None, end=None, limit=None, timeframe = TimeFrame.Day):

    #Format start and end dates
    time_param_arr = Format_Datetime(start_date = start, end_date = end ,time_frame= timeframe,limit= limit)

    #Formulate request
    request = StockBarsRequest(symbol_or_symbols = symbol_or_symbols, timeframe= timeframe, start= time_param_arr[0], end=time_param_arr[1])
    barset_returned = api.get_stock_bars(request_params=request).df

    #Return dataframe
    return barset_returned

    
    #Calculates todays date for end date and parse parameters to pass to datetime object
    #todays_date = date.today()
    #end_date_year = todays_date.strftime("%Y")
    #end_date_month = todays_date.strftime("%m")
    #end_date_day = todays_date.strftime("%d")
    #today_datetime_obj = datetime(end_date_year, end_date_month, end_date_day)

    #print("d1 =", end_date_day)

    #Formulate request
    #request = StockBarsRequest(symbol_or_symbols = symbol_or_symbols, timeframe= TimeFrame.Day, start=datetime(2023, 1, 1))
    #barset_returned = api.get_stock_bars(request_params=request).df

    #Return dataframe
    #return barset_returned
    

