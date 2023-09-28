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

#imports added
from Taylor_package.format_M import Format_Datetime_Monthly
from Taylor_package.format_D import Format_Datetime_Daily



#Constants (Default amount of bars to pull)
DAY_LIMIT_DEFAULT = 365

def Format_Timeframe_String(timeframe = "1Day"):

    #If the input is already in Timeframe object pass through
    if(type(timeframe) == type(TimeFrame.Day)):
        return [TimeFrame.Day, "1Day"] 

    #If a string is passed in convert to appropriate Timeframe object
    elif(isinstance(timeframe,str)):

        #Monthly
        if(("Monthly" in timeframe) or ("Month" in timeframe) or ("1Month" in timeframe)):
            return [TimeFrame.Month, "1Month"]
        #Weekly
        if(("Weekly" in timeframe) or ("Week" in timeframe) or ("1Week" in timeframe)):
            return [TimeFrame.Week, "1Week"]
        #3 Day
        if(("3D" in timeframe) or ("3 Day" in timeframe) or ("3Day" in timeframe)):
            return [TimeFrame.Day, "3Day"]        
        #Daily
        if(("Daily" in timeframe) or ("Day" in timeframe) or ("1Day" in timeframe)):
            return [TimeFrame.Day, "1Day"] 
        #4 Hour
        if(("4H" in timeframe) or ("4 Hour" in timeframe) or ("4 Hour" in timeframe)):
            return [TimeFrame.Hour, "4Hour"] 
        #2 Hour
        if(("2H" in timeframe) or ("2 Hour" in timeframe) or ("2 Hour" in timeframe)):
            return [TimeFrame.Hour, "2Hour"]
        #Hourly
        if(("Hourly" in timeframe) or ("Hour" in timeframe)):
            return [TimeFrame.Hour, "1Hour"]
        #30 Minute
        if(("30M" in timeframe) or ("30 Min" in timeframe) or ("30Min" in timeframe) or ("30Minute" in timeframe) or ("30 Minute" in timeframe)):
            return [TimeFrame.Minute, "30Minute"]
        #15 Minute
        if(("15M" in timeframe) or ("15 Min" in timeframe) or ("15Min" in timeframe) or ("15Minute" in timeframe) or ("15 Minute" in timeframe)):
            return [TimeFrame.Minute, "15Minute"]
        #5 Minute
        if(("5M" in timeframe) or ("5 Min" in timeframe) or ("5Min" in timeframe) or ("5Minute" in timeframe) or ("5 Minute" in timeframe)):
            return [TimeFrame.Minute, "5Minute"]
        #1 Minute
        if(("1M" in timeframe) or ("1 Min" in timeframe) or ("1Min" in timeframe) or ("1Minute" in timeframe) or ("1 Minute" in timeframe)):
            return [TimeFrame.Minute, "1Minute"]

        #Couldn't Identify Target timeframe
        else:
            logger.error("Couln't identify valid timeframe to pull historical data for") 




# #####   MAIN DRIVER FUNCTION FOR PULLING HISTORICAL BARS   #####
# #Format datetime into datetime objects
# #Note 1 day added to end date to correct API request to alpacca and pull todays/that days data
def Format_Datetime(start_date = None, end_date = None, time_frame = "1Day", limit = 100):

    #Based on Timeframe, formulate start and end date to relevant dates (4 HR needs to be formatted with hours...)

    #Daily Timeframe
    if(time_frame == "1Day"):
        arr = Format_Datetime_Daily(start_date = start_date, end_date = end_date, time_frame = TimeFrame.Day, limit = None)
        return arr
    
    #Monthly Timeframe
    if(time_frame == "1Month"):
        arr = Format_Datetime_Daily(start_date = start_date, end_date = end_date, time_frame = TimeFrame.Month, limit = None)
        return arr


