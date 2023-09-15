from sqlalchemy import create_engine # pip install SQLAlchemy
from sqlalchemy.engine import URL
import pypyodbc # pip install pypyodbc
import pandas as pd # pip install pandas

SERVER_NAME = '<SERVER NAME>'
DATABASE_NAME = '<DATABASE NAME>'
TABLE_NAME = '<TARGET TABLE NAME>'

excel_file = '<file path>'

connection_string = f"""
    DRIVER={{SQL Server}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trusted_Connection=yes;
"""
connection_url = URL.create('mssql+pyodbc', query={'odbc_connect': connection_string})
enigne = create_engine(connection_url, module=pypyodbc)

excel_file = pd.read_excel(excel_file, sheet_name=None)
for sheet_name, df_data in excel_file.items():
    print(f'Loading worksheet {sheet_name}...')
    # {'fail', 'replace', 'append'}
    df_data.to_sql(TABLE_NAME, enigne, if_exists='append', index=False)