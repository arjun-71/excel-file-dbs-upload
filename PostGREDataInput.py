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
import HelperMethods.header2 as hds     
import HelperMethods.header3 as hds2
import csv

# Replace {key} with your actual database connection details
databaseConnectionString = dbs.db_url
engine = create_engine(databaseConnectionString)   

#create a dictionary with the new csv file name as the key value and the corresponding budgetData created as the value pair
file_budget_mapping = {}

# Create a list to store BudgetData objects
budget_data_list = []        #declare this as global variable     



#name of the resultant csv file
resultant_file = 'resultant_file.csv'



#file entry point
#the function for entry of the file 






#extracting the file path
filePath = fp.get_excel_file_path("sample_construction_file_1.xlsx")

#converting excel file to csv file
#start here

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



#checking the functionality of new csv generator engine

resultant_file = hds2.generate_project_csv(name_of_the_project, budgetData.get_value([name_of_the_project]), project_code)
print(f'CSV file "{resultant_file}" has been created for the project "{name_of_the_project}".')


df = pd.read_csv(resultant_file)

#print(df.head(30))

fourth_column = df.iloc[:, 3] 
print(fourth_column)

#the following adds and maps the new object created and maps it to the required file name
budget_data_list.append(budgetData)
file_budget_mapping[new_csv_file_name] = budgetData

#print(budget_data_list[0].get_value(['Polytechnic Zoom Classrooms & Space Upgrades','Construction Costs','Renovation']))
for fileName, budgetData in file_budget_mapping.items():
     print(f"File Name: {fileName}")
     print(f"budget data {budgetData.get_value(['Polytechnic Zoom Classrooms & Space Upgrades','Construction Costs','Renovation'])}")

# List of values to set in the fourth column
new_values = ['X', 'Y', 'Z', 'W']

# Loop through the DataFrame and set values in the fourth column one by one
for i, value in enumerate(new_values):
    df.at[i, 'Unnamed: 3'] = value      #plugging in the values
print(df.head())





# Read the CSV file into a DataFrame


# Loop through all rows in the DataFrame
for index, row in df.iterrows():
    # Access values in each column for the current row
    column1_value = row['Land Acquisition']
    column2_value = row['Land Acquisition.1']
    column3_value = row['At Construction Budget']

    

    # Process or print the values as needed
   #getting the corresponsding value from the budgetData
    






     
     
     


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