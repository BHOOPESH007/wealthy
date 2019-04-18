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

def get_statics_data(stock_holder_details, value):
    if is_empty(value):
        return 0,0,0
    min_stock_price_index = stock_holder_details['StockPrice'].index(min(value))
    max_stock_price_index = stock_holder_details['StockPrice'].index(max(value))
    profit =STOCK_UNIT*(stock_holder_details['StockPrice'][max_stock_price_index] - stock_holder_details['StockPrice'][min_stock_price_index])
    return stock_holder_details['StockDate'][min_stock_price_index], stock_holder_details['StockDate'][max_stock_price_index], profit

def is_empty(value):
    if not value:
        return True
    return False