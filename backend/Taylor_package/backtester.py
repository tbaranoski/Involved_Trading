from datetime import datetime, date, timedelta

def backtest(start_date = "2020-01-01", end_date = "2023-01-01"):
    start_obj = datetime.strptime(start_date, "%Y-%m-%d")
    end_obj = datetime.strptime(end_date, "%Y-%m-%d")

    temp_day = start_obj

    #Increment one day at a time
    while(temp_day != end_obj):
        temp_day = temp_day + (timedelta(days=1))
        strategy(temp_day)



#In the past:
def strategy_function(current_day):




class Strategy:
    def __init__(self, current_day, triggers, num_triggers, timeframe_triggers):
        self.current_day = current_day

        #
        self.current_trigger = 
        self.triggers = [trigger1(),trigger2(),trigger3()]
        self.num_triggers = 1
        self.timeframe_triggers = ["1Day", "1HR", "5MIN"]


    def trigger1(self):
        #Pull last 20 days of Dialy bars
        triggered = None
        if triggered:
            self.current_trigger += 1
            trigger2()
        else:
            self.current_trigger = 0

    def trigger2():
        #Pull last 20HR of 1HR bars

    def trigger3():
        #Pull last 5 MIN of 5MIN bars
        #recursivelly look at all previosu timeframes
##############################################################################
#Driver Function
def driver():
    print("Start Backtester")

    Strat1 = Strategy()
    Strat2 = Strategy()

    backtest(start_date ="2020-01-01", end_date="2023-01-01")
driver()
    