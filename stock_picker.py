import sys
from csvreader import CSVReader
from process import start_process

if __name__ == "__main__":
    file_name = sys.argv[1]
    stock_dict = CSVReader(file_name).read_csv()
    start_process(stock_dict)