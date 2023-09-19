import pandas as pd
from ExcelFilePathReturn import get_excel_file_path

# Get the Excel file path using the get_excel_file_path() function
excel_path = get_excel_file_path()

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_path)

# Now you can work with the 'df' DataFrame in your current Python file

reached_land_acquisition = False

# Convert column names to strings and print the header row
header = df.head()
print(header)

# Iterate through the rows
for index, row in df.iterrows():
    # Check if the value in the "Unnamed: 1" column is "Land Acquisition"
    if row['Unnamed: 1'] == 'Land Acquisition':
        reached_land_acquisition = True
    
    # Format and print the row with tabs
    formatted_row = "\t".join(map(str, row))
    print(formatted_row)
    
    # Stop iterating if we reached "Land Acquisition"
    if reached_land_acquisition:
        break
