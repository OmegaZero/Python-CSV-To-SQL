#!/usr/bin/python

import pandas as pd
from sqlalchemy import create_engine
import sys, getopt, pyodbc

def load_csv_to_sql(file_path):
  
  ODBC_DRIVER='ODBC Driver 17 for SQL Server'

  # Load the CSV into a pandas DataFrame
  df = pd.read_csv(file_path, header=None, names=['ID', 'First Name', 'Last Name', 'Address'])

  # Create the connection string for SQLAlchemy
  if _username and _password:
      conn_str = f"mssql+pyodbc://{_username}:{_password}@{_server}/{_database}?driver={ODBC_DRIVER}"
  else:
      # Use Windows Authentication if no username and password are provided
      conn_str = f"mssql+pyodbc://{_server}/{_database}?driver={ODBC_DRIVER}&trusted_connection=yes"

  # Create the SQLAlchemy engine with pyodbc connection
  engine = create_engine(conn_str, fast_executemany=True)

  # Load CSV into a pandas DataFrame
  df = pd.read_csv(file_path, header=None, names=['ID', 'First Name', 'Last Name', 'Address'])

  # Insert the DataFrame into the SQL Server table
  with engine.begin() as conn:
      df.to_sql(_table_name, conn, if_exists='append', index=False)

def main():

  global _server, _database, _table_name, _username, _password

  _server = 'TestDev'
  _database = 'MyTestDB'
  _table_name = 'TestCSV'
  _username = None
  _password = None
  file_path = 'test.csv'

  print("starting program...")

  load_csv_to_sql(file_path)

  print("program completed...")

if __name__=="__main__":
  main()