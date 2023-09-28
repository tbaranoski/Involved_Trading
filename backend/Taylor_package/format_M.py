from datetime import datetime, date, timedelta
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
from Logging_Backend.base_logger import logger


#Formats Datetime for Monthly Timeframe
def Format_Datetime_Monthly(start_date = None, end_date = None, time_frame = TimeFrame.Month, limit = None):

    #Get todays Date and Set variables up
    todays_date = date.today()
    end_datetime_obj = None
    start_datetime_obj = None

    today_date_year = int(todays_date.strftime("%Y"))
    today_date_month = int(todays_date.strftime("%m"))
    today_date_day = int(todays_date.strftime("%d"))
    today_obj = datetime(today_date_year, today_date_month, today_date_day)

    
    #If no end date passed in, today is end date
    if(end_date == None):        
        end_datetime_obj = today_obj
                
    #If end_date was given in correct datetime object format, pass through function
    elif((type(end_date)) == type(datetime(2022,1,1))):
        end_datetime_obj = end_date
        
        #If date is before today add one day to get data
        if(end_datetime_obj < today_obj):
            end_datetime_obj = end_datetime_obj + (timedelta(days=1))
        else:
            pass

    #A string was passed in, reformat
    #Format passed in 07/01/2023
    elif(isinstance(end_date,str)):
        try:
            date_array = end_date.split('/')
            end_datetime_obj = datetime(int(date_array[2]), int(date_array[0]), int(date_array[1]))
        except:
            logger.error("End Date could not be parsed. Check End Date passed in")

        #If date is before today add one day to get data
        if(end_datetime_obj < today_obj):
            end_datetime_obj = end_datetime_obj + (timedelta(days=1))
        else:
            pass


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
        try:
            date_array = start_date.split('/')
            start_datetime_obj = datetime(int(date_array[2]), int(date_array[0]), int(date_array[1]))
        except:
            logger.error("Start Date could not be parsed. Check Start Date passed in")
        
        

    ###############################################################################
    ###   ERROR CHECK (Make sure start date is before end date)   ###
    if(start_datetime_obj >= end_datetime_obj):
        logger.error("Start Date and End Date Reversed")

    return [start_datetime_obj,end_datetime_obj]