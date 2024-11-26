
# Hadoop + PostgreSQL on Docker

This project sets up a Dockerized architecture including:
- A PostgreSQL database
- Hadoop HDFS with 1 NameNode and 2 DataNodes

# 1. Connect to the postgres database .

    docker exec -it postgres  psql -U postgres         


# 2 . test if our hadoop is set up  namenode , datanode1 , datanode2

     docker exec -it namenode bash 

     hdfs dfsadmin -report 


 If everything is OK, we can load the file from Kaggle, 'Full IMDb Dataset,' and import it into our PostgreSQL    database using a Python script that we will create .

load_data_to_db.py
URL = https://www.kaggle.com/api/v1/datasets/download/octopusteam/full-imdb-dataset

docker exec -it postgres  psql -U postgres

<img width="727" alt="Capture d’écran 2024-11-26 à 15 09 43" src="https://github.com/user-attachments/assets/06f4bce0-e001-4e62-b174-4f39ac8c1c89">


 

 # 4. Next, we will extract data from the database, transform it into a CSV format, and load it into Hadoop 
     fromdb_tohadoop.py
    
     The process in the script is broken down into three main stages:
     Extracting data from PostgreSQL,
     Transforming data into a CSV file, 
     and Loading the data into Hadoop HDFS.

<img width="675" alt="Capture d’écran 2024-11-26 à 15 18 16" src="https://github.com/user-attachments/assets/53f2730f-9948-4a32-a298-17d1f2f6e8da">

#5 I am going to add Apache Spark to interact with the data in Hadoop.
