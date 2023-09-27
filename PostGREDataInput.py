from sqlalchemy import create_engine
import psycopg2
import pandas as pd
import HelperMethods.FilePathReturn as  fp
import numpy as np
import HelperMethods.DatabaseString as dbs
import HelperMethods.ExcelToCsv as converter


# Replace {key} with your actual database connection details
databaseConnectionString = dbs.db_url
engine = create_engine(databaseConnectionString)    #set database string 

output_csv_file = 'output_csv_file.csv'

#extracting the file path
filePath = fp.get_excel_file_path()
print(filePath)

#converting excel file to csv file
csv = converter.fileConverter(filePath)             
print(csv.head())

# def extract_and_insert_single_sheet(sheet_name, excel_file, table_name):
#     df = pd.read_excel(excel_file, sheet_name)
#     df.to_sql(name=table_name, con=engine, if_exists='append', index=False)

# # Replace 'main.xlsx' with the actual path to your Excel file
# excel_file_path = filePath
# sheet_name_to_process = 'Sheet1'  # Replace with the desired sheet name
# table_name_to_insert = dbs.table_name  # Replace with the desired table name

# extract_and_insert_single_sheet(sheet_name_to_process, excel_file_path, table_name_to_insert)