from sqlalchemy import create_engine
import psycopg2
import pandas as pd
import HelperMethods.FilePathReturn as  fp
import numpy as np
import HelperMethods.DatabaseString as dbs
import HelperMethods.ExcelToCsv as converter
import HelperMethods.csv_name_changer as nameChanger
import dataManagement.hash_function
import dataManagement.dataBody as dsn 
import dataManagement.dataBody

# Replace {key} with your actual database connection details
databaseConnectionString = dbs.db_url
engine = create_engine(databaseConnectionString)    #set database string 

budgetData = dataManagement.dataBody.BudgetData()


#extracting the file path
filePath = fp.get_excel_file_path("sample_construction_file_1.xlsx")
print(filePath)

#converting excel file to csv file
csv = converter.fileConverter(filePath)             

first_row = csv.iloc[0]
first_column = csv.iloc[:, 0]

#the following variable contains the name mentioned in the file
name_in_the_file =first_column.iloc[0] 
name_of_the_project = csv.columns[3]
project_code = csv.columns[0]

# Generate a new CSV file name without spaces
new_csv_file_name = nameChanger.return_Csv_File_Name(name_of_the_project, project_code)

# Save the DataFrame to the new CSV file
csv.to_csv(new_csv_file_name, index=False)

# Read and print the first few rows of the new CSV file
new_csv_data = pd.read_csv(new_csv_file_name)


# Loop through every row and print the value of every column field 

field_List = []
for index, row in new_csv_data.iterrows():
    #print(f"Row {index}:")
    if index == 0 :
        
        for column_name, value in row.items():
            
            field_List.append(value)
    
           
    else:
        break

key_one = ""
#print(field_List)



for index, row in new_csv_data.iterrows():
    print(f"Row {index}:")

    for column_name, value in row.items():
        if index == 0 and value == "Current Budget":
            project_name = column_name
            print(project_name)             #the following contains the project name of the sheet
        if column_name == "Unnamed: 1" and value != "0" and pd.notna(value) and  index >1:
            section_value = value
            #print(section_value) the following contains the section value input file
            
        if pd.notna(value):

            #print(f" '{column_name}': {value}")
            column_field_value = budgetData.replace_value(column_name)
            print(f" '{column_field_value}': {value}")

            
            #use the insert function here please


                
#print(field_List)  #the following list contains the list of all major fields for the above costs  

 

#creating a dictionary data structure for storing  values 


# def extract_and_insert_single_sheet(sheet_name, excel_file, table_name):
#     df = pd.read_excel(excel_file, sheet_name)
#     df.to_sql(name=table_name, con=engine, if_exists='append', index=False)

# # Replace 'main.xlsx' with the actual path to your Excel file
# excel_file_path = filePath
# sheet_name_to_process = 'Sheet1'  # Replace with the desired sheet name
# table_name_to_insert = dbs.table_name  # Replace with the desired table name

# extract_and_insert_single_sheet(sheet_name_to_process, excel_file_path, table_name_to_insert)