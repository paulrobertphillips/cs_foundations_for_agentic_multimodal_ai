from tools.io_tools import read_csv
from processing.data_tools import filter_rows

rows = read_csv("data.csv")
print(filter_rows(rows))