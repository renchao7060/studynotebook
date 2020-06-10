from excel_magic.dataset import Dataset
import os
print(os.getcwd())

file_name = '年度财务报告.xlsx'

excel_file=Dataset(file_name)
excel_file.split_sheets_to_file()