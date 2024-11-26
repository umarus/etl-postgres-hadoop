import psycopg2
import pandas as pd
import subprocess
import logging

# PostgreSQL database configuration
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'hadoopdb'
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'

# Hadoop HDFS configuration
HDFS_DIR = '/user/root/hadoop'
LOCAL_TMP_DIR = '/tmp'
CSV_FILE = f'{LOCAL_TMP_DIR}/imdb.csv'

# Log file configuration
LOG_FILE = 'fromdb_tohadoop.log'
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def extract_data_from_postgresql():
    try:
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

        logging.info("Executing the query to extract data")
        # Execute the query to extract data
        query = "SELECT * FROM imdb"
        df = pd.read_sql_query(query, conn)

        logging.info("Saving data to CSV file")
        # Save the data to a CSV file
        df.to_csv(CSV_FILE, index=False)

        cursor.close()
        conn.close()
        logging.info(f"Data extracted and saved to {CSV_FILE}")
    except Exception as e:
        logging.error(f"Error extracting data from PostgreSQL: {e}")

def load_data_into_hdfs():
    try:
        logging.info("Copying the CSV file to the NameNode")
        # Copy the CSV file to the NameNode
        subprocess.run(['docker', 'cp', CSV_FILE, 'namenode:/tmp/'], check=True)

        logging.info("Loading the CSV file into HDFS")
        # Load the CSV file into HDFS
        #subprocess.run(['docker', 'exec', 'namenode', 'hdfs', 'dfs', '-mkdir', '-p', HDFS_DIR], check=True)
        subprocess.run(['docker', 'exec', 'namenode', 'hdfs', 'dfs', '-put', f'/tmp/imdb.csv', HDFS_DIR], check=True)

        logging.info(f"Data loaded into HDFS at {HDFS_DIR}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error loading data into HDFS: {e}")

def main():
    logging.info("Starting the script")
    extract_data_from_postgresql()
    load_data_into_hdfs()
    logging.info("Script completed successfully")

if __name__ == '__main__':
    main()