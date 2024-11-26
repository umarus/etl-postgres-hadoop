import pandas as pd
import psycopg2
from psycopg2 import sql
import logging

# PostgreSQL database configuration
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'hadoopdb'
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'

# Path to the CSV file
CSV_FILE = './data/data.csv'
#https://www.kaggle.com/api/v1/datasets/download/octopusteam/full-imdb-dataset

# Name of the table to create
TABLE_NAME = 'imdb'

# Log file configuration
LOG_FILE = 'load_csv_into_postgres.log'
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def create_table_from_csv():
    try:
        logging.info("Reading the CSV file")
        # Read the CSV file
        df = pd.read_csv(CSV_FILE)

        logging.info("Connecting to the PostgreSQL database")
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()

        logging.info("Generating the SQL query to create the table")
        # Generate the SQL query to create the table
        columns = df.columns
        column_definitions = []
        for col in columns:
            col_type = 'TEXT'  # Default to TEXT for all columns
            if df[col].dtype == 'int64':
                col_type = 'INTEGER'
            elif df[col].dtype == 'float64':
                col_type = 'FLOAT'
            column_definitions.append(f"{col} {col_type}")

        create_table_query = sql.SQL("CREATE TABLE IF NOT EXISTS {} ({})").format(
            sql.Identifier(TABLE_NAME),
            sql.SQL(', ').join(map(sql.SQL, column_definitions))
        )

        logging.info("Executing the query to create the table")
        # Execute the query to create the table
        cursor.execute(create_table_query)
        conn.commit()
        cursor.close()
        conn.close()
        logging.info(f"Table {TABLE_NAME} created successfully")
    except Exception as e:
        logging.error(f"Error creating table: {e}")

def insert_data_from_csv():
    try:
        logging.info("Reading the CSV file")
        # Read the CSV file
        df = pd.read_csv(CSV_FILE)

        logging.info("Connecting to the PostgreSQL database")
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()

        logging.info("Inserting the data into the table")
        # Insert the data into the table
        tuples = [tuple(x) for x in df.to_numpy()]
        cols = ', '.join(list(df.columns))
        query = f"INSERT INTO {TABLE_NAME} ({cols}) VALUES ({', '.join(['%s'] * len(df.columns))})"
        cursor.executemany(query, tuples)
        conn.commit()
        cursor.close()
        conn.close()
        logging.info("Data inserted successfully")
    except Exception as e:
        logging.error(f"Error inserting data: {e}")

def main():
    logging.info("Starting the script")
    create_table_from_csv()
    insert_data_from_csv()
    logging.info("Script completed successfully")

if __name__ == '__main__':
    main()
