import csv, datetime

class CSVReader:
    def __init__(self, file_path):
        self.file_name = file_path
        self.csv_reader = []
        self.StockDate_index = None
        self.stock_dict = {}

    def read_columns_name(self, first_row):
        columns_name=[]
        for cell_data in first_row:
            columns_name.append(cell_data)
        return columns_name

    def read_entries(self, stock_holder_name, row_data, columns_name):
        
        for index, cell_data in enumerate(row_data[1:]):
            if columns_name[index+1] =='StockDate':
                if not cell_data:
                    cell_data = self.stock_dict[stock_holder_name][columns_name[index+1]][-1]
                cell_data = convert_datatime_object(cell_data)
            
            elif columns_name[index+1] =='StockPrice':
                cell_data=float(cell_data)
            self.stock_dict[stock_holder_name][columns_name[index+1]].append(cell_data)
        self.stock_dict[stock_holder_name]['count']+=1

    def create_new_account(self, stock_holder_name, row_data, columns_name):
        self.stock_dict[stock_holder_name]={'count':1}
        for index, cell_data in enumerate(row_data[1:]):
            if columns_name[index+1] =='StockDate':
                cell_data = convert_datatime_object(cell_data)
            
            elif columns_name[index+1] =='StockPrice':
                cell_data=float(cell_data)
            self.stock_dict[stock_holder_name][columns_name[index+1]]=[cell_data]

    def read_csv(self):
        with open(self.file_name, 'r') as csv_file:
            self.csv_reader = list(csv.reader(csv_file, delimiter=','))
        
        columns_name=self.read_columns_name(self.csv_reader[0])

        self.StockDate_index = columns_name.index('StockDate')

        for row_data in self.csv_reader[1:]:
            stock_holder_name = row_data[0]
            
            if stock_holder_name in self.stock_dict:
                self.read_entries(stock_holder_name, row_data, columns_name)
            else:
                self.create_new_account(stock_holder_name, row_data, columns_name)
        return self.stock_dict

def convert_datatime_object(str_data):
    try:
        str_data = str_data.replace('/', '-')
        month = str_data.split('-')[1]
        if month.isdigit():
            return datetime.datetime.strptime(str_data, '%d-%M-%Y').date()
        return datetime.datetime.strptime(str_data, '%d-%b-%Y').date()
    except:
        raise Exception('invalid date time format')
    