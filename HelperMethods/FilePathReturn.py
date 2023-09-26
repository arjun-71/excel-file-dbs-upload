import pandas as pd
import os

def get_excel_file_path():
    # Replace 'your_excel_file.xlsx' with the actual name of your Excel file
    excel_filename = 'SampleStudentRecord.xlsx'

    # Get the absolute path to the current working directory
    current_directory = os.getcwd()

    # Combine the current directory and the Excel filename to get the full path
    excel_file_path = os.path.join(current_directory, excel_filename)
    
    return excel_file_path

# Get the Excel file path using the get_excel_file_path() function
excel_path = get_excel_file_path()

# Read the Excel file into a DataFrame
#df = pd.read_excel(excel_path)
#print(df.head())

excel_file = pd.read_excel(excel_path, sheet_name=None)
#for sheet_name, df_data in excel_file.items():
    #print('Loading worksheet {sheet_name}...')
    

    # {'fail', 'replace', 'append'}
#df_data.to_sql(TABLE_NAME, enigne, if_exists='append', index=False)

