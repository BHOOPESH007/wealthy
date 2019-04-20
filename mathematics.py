STOCK_UNIT = 100
def get_mean_SD(value):
    n=len(value)
    if is_empty(value):
       return 0,0
    mean_value = sum(value)/n
    distance = 0
    for one_value in value:
        distance = distance + (one_value-mean_value)**2
    standard_deviation = (distance/n)**0.5
    return mean_value, standard_deviation

def get_statics_data(value, StockDates_within_dates):
    if is_empty(value):
        return 0,0,0
    min_stock_price_index, max_stock_price_index, profit_per_unit =get_max_profit(value, len(value))
    if min_stock_price_index is None:
        return 0,0,0
    profit =STOCK_UNIT*profit_per_unit
    return StockDates_within_dates[min_stock_price_index], StockDates_within_dates[max_stock_price_index], profit

def is_empty(value):
    if not value:
        return True
    return False

def get_max_profit(arr, n): 
    max_profit = -1000
    maxRight = arr[n - 1]  
    maxRight_index = n-1
    left_index= None
    right_index = None
    for i in range(n - 2, -1, -1): 
        if (arr[i] > maxRight): 
            maxRight = arr[i] 
            maxRight_index = i
        else: 
            diff = maxRight - arr[i] 
            if (diff > max_profit):
                left_index= i
                right_index = maxRight_index
                max_profit = diff 
    return left_index, right_index, max_profit 