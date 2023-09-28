import requests
import pandas as pd
from datetime import datetime,timedelta
import json
import numpy as np
from Logging_Backend.base_logger import logger
import os
import exception
import os
import calendar

url = "https://data.alpaca.markets/v2/stocks/bars?symbols=AAPL&timeframe=1Day&start=2012-01-03&end=2022-01-04&limit=1000&adjustment=raw"


#Get Stock Bars
def getStockData(symbol, timeframe, start, end, limit = None):
        
    #Monthly Notes: End date needs to be the first day of the next month    
    #Start: 2023-01-06 -> 2023-01-01 (first calender day of month)
    #End: 2023-05-21 -> 2023-05-31 (last calender day of month)
    #edge case: If end date is the current month, then end date is today

    #Monthly TimeFrame
    if(timeframe=="1Month"):
        
        #Format Start Date to First of Month
        start_date_o = datetime.strptime(start, "%Y-%m-%d")
        start_first_day = start_date_o.replace(day=1)
        start = start_first_day.strftime("%Y-%m-%d")
        logger.info("Start Date: " + start)
        print(type(start))

        #Format End Date to Last of Month
        end_date_o = datetime.strptime(end, "%Y-%m-%d")

        #If end date is current month, end date=current day
        current_date = datetime.now().date()        
        if((end_date_o.month == current_date.month) and (end_date_o.year == current_date.year)):
            current_day = current_date.day
            updated_date = end_date_o.replace(day=current_day -1)
            end = updated_date.strftime("%Y-%m-%d")
            logger.info("End Date (Should be todays date): " + end)
        else:   
            end_first_day = end_date_o.replace(day=(calendar.monthrange(end_date_o.year, end_date_o.month)[1]))
            end = end_first_day.strftime("%Y-%m-%d")
            logger.info("End Date: " + end)
    
    #Daily TimeFrame
    if(timeframe=="1Week"):
        pass


    #Daily TimeFrame
    if(timeframe=="1Day"):
        pass



    #Make Bar requets to API endpoint
    return (Request_Bars(symbol = symbol, timeframe = timeframe, start = start, end = end, limit = limit))
        
        
        
        
#Main Driving funciton to pull Bars for specified timeframe
def Request_Bars(symbol, timeframe, start, end, limit = None):

    print("timeframe " + timeframe)
    print("start " + start)
    print("end " + end)

    #Attempt to get API bars for specified Timeframe
    try:
        symbol = symbol.upper()
        url = f"https://data.alpaca.markets/v2/stocks/bars?symbols={symbol}&timeframe={timeframe}&start={start}&end={end}&limit={limit}&adjustment=raw"
        
        headers = {
            "accept": "application/json",
            "APCA-API-KEY-ID": os.environ.get('ALPACA_KEY'),
            "APCA-API-SECRET-KEY": os.environ.get('ALPACA_SECRET')
        }

        response = requests.get(url, headers=headers)
        logger.debug(response.text)
        response = json.loads(response.text) 

        formatted_array = response['bars'][symbol]
        df = pd.DataFrame(formatted_array)
        df = df.rename(columns= {"t": "timestamp","o": "open","h":"high","l":"low", "c":"close","v":"volume","n":"trade_count","vw":"vwap"})
        
        #Change timestamp from float64 to datetime[ns, UTC]
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df["symbol"] = symbol 
        df["volume"] = df["volume"].astype(np.float64)
        df = df.set_index(["symbol","timestamp"])
        
        logger.info("Successful: Historic data pulled via custom endpoint")
        return df
    
    except Exception as err:
        logger.error("Error getting Bars from Alpaca Endpoint"+str(err))
