from datetime import datetime
from typing import Dict
import pandas as pd

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

"""
    Retrieves daily bars for a specified symbol and time period from Alpaca's API.

    Args:
        api (alpaca_trade_api.REST): An instance of Alpaca's REST API class.
        symbol (str): The symbol for which to retrieve bars.
        start_time (str): The start time for the bar query in 'YYYY-MM-DDTHH:MM:SSZ' format.
        end_time (str): The end time for the bar query in 'YYYY-MM-DDTHH:MM:SSZ' format.
        limit (int): The maximum number of bars to retrieve.

    Returns:
        dict: A dictionary containing the retrieved bars, organized by symbol.
    """

#Returns Dataframe of Data for ticker
def Get_D_Bars(api = None, symbol_or_symbols = None, start= None, end=None, limit=None):

    #Configure request object and make API request
    request = StockBarsRequest(symbol_or_symbols=symbol_or_symbols, timeframe=TimeFrame.Day, start=start, end=end, limit=limit)
    barset_D_temp = api.get_stock_bars(request_params=request).df

    print(barset_D_temp)
  
