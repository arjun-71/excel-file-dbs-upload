import csv
import os

def create_csv_file(column_headings, data, file_name, output_folder='.'):
    try:
        # Create the full file path
        file_path = os.path.join(output_folder, file_name)

        # Ensure the output folder exists, create it if it doesn't
        os.makedirs(output_folder, exist_ok=True)

        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(column_headings)  # Write the column headings
            writer.writerows(data)  # Write the data

        return file_path
    except Exception as e:
        return f"Error: {str(e)}"
