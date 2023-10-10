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
import HelperMethods.InformationToObject as objectInserter

# Replace {key} with your actual database connection details
databaseConnectionString = dbs.db_url
engine = create_engine(databaseConnectionString)   

#create a dictionary with the new csv file name as the key value and the corresponding budgetData created as the value pair
file_budget_mapping = {}

# Create a list to store BudgetData objects
budget_data_list = []        #declare this as global variable        

#extracting the file path
filePath = fp.get_excel_file_path("sample_construction_file_1.xlsx")

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
print(new_csv_file_name)

# Save the DataFrame to the new CSV file
csv.to_csv(new_csv_file_name, index=False)

# Read and print the first few rows of the new CSV file
new_csv_data = pd.read_csv(new_csv_file_name)

# the following object created contains the lew object of type cost 
budgetData = objectInserter.process_csv_data(new_csv_data)   


#the following adds and maps the new object created and maps it to the required file name
budget_data_list.append(budgetData)
file_budget_mapping[new_csv_file_name] = budgetData     
print(budget_data_list[0].get_value(['Polytechnic Zoom Classrooms & Space Upgrades','Construction Costs','Renovation']))
for fileName, budgetData in file_budget_mapping.items():
     print(f"File Name: {fileName}")
     print(f"budget data {budgetData.get_value(['Polytechnic Zoom Classrooms & Space Upgrades','Construction Costs'])}")


#print (budgetData['Polytechnic Zoom Classrooms & Space Upgrades']['Construction Costs']['Renovation'])
            
            #use the insert function here please
#print(project_code_value)
#print(budgetData.get_value(['Polytechnic Zoom Classrooms & Space Upgrades']))
#print(budgetData.get_value(['Polytechnic Zoom Classrooms & Space Upgrades', 'Land Acquisition', 'Land Acquisition', 'At Construction Budget']))  # This will print 'new_value'

                
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