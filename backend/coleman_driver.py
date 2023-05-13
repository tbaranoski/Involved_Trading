
from Coleman_package.get_historical_data import Get_D_Bars
from Config_Alpaca_Clients.config_client import Configure_Client,Configure_Historical_Data_Client




#Main Program driver for Taylor
def Coleman_Driver():
 
    #####   GET CLIENT OBJECTS   #####
    ##  Trading Client: For placing trades
    ##  historical_data_client: For fetching historical data    
    trading_client = Configure_Client()
    historical_data_client = Configure_Historical_Data_Client()


    #Test getting data
    bars_D = Get_D_Bars(historical_data_client, symbol_or_symbols="AAPL")


