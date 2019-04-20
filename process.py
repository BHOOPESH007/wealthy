import datetime
from difflib import get_close_matches 
from csvreader import CSVReader, convert_datatime_object
from mathematics import get_mean_SD, get_statics_data, is_empty

def start_process(stock_dict):
    REPEAT = 'y'
    
    while REPEAT in ['y', 'Y']:
        flag = 'y'
        stock_holder_name = raw_input('"Welcome Agent! Which stock you need to process?":- ')
        #search stock_holder_name is exist or not
        if not stock_holder_name in stock_dict:
            suggested_stock_holder_name = get_close_matches(stock_holder_name.lower(), stock_dict.keys()) + get_close_matches(stock_holder_name.upper(), stock_dict.keys())
            
            if suggested_stock_holder_name:
                flag = raw_input('"Oops! Do you mean '+ suggested_stock_holder_name[0] +'? y or n":- ') 
                if flag in ['y', 'Y']:
                    stock_holder_name = suggested_stock_holder_name[0]
                elif flag in ['n', 'N']:
                    return
            else:
                print '"Oops! '+ stock_holder_name +' not found in our record\n start again"'
                start_process(stock_dict)
                return 
        
            
        
        stock_holder_details = stock_dict.get(stock_holder_name,None)

        start_date = raw_input('"From which date you want to start":- ')
        start_date = convert_datatime_object(start_date)
        end_date = raw_input('"Till which date you want to analyze":- ')
        end_date = convert_datatime_object(end_date)


        StockDates = stock_holder_details.get('StockDate',[])
        StockPrices = stock_holder_details.get('StockPrice', None)
        StockPrice_within_dates=[]
        StockDates_within_dates=[]

        for index, StockDate in enumerate(StockDates):
            if StockDate>=start_date and StockDate<= end_date:
                StockPrice_within_dates.append(StockPrices[index])
                StockDates_within_dates.append(StockDate)
        
        if is_empty(StockPrice_within_dates):
            print 'Oops!, No record Found'
        else:
            mean_value, standard_deviation = get_mean_SD(StockPrice_within_dates)
            buy_date, sell_date, profit = get_statics_data(StockPrice_within_dates, StockDates_within_dates)

            print '"Here is you result":- \nMean: ',mean_value, '\nStd: ',standard_deviation, '\nBuy date: ',buy_date, '\nSell date: ',sell_date, '\nProfit: Rs. ',profit

        REPEAT = raw_input("Do you want to continue? (y or n):- ")
        if not REPEAT in ['y', 'Y', 'n', 'N']:
            print REPEAT, " it's invalid input"
            REPEAT = raw_input("Do you want to continue? (y or n):- ")
