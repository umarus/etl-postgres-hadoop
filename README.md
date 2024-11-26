
# Hadoop + PostgreSQL on Docker

This project sets up a Dockerized architecture including:
- A PostgreSQL database
- Hadoop HDFS with 1 NameNode and 2 DataNodes

# 1. Connect to the postgres database .

    docker exec -it postgres  psql -U postgres         


# 2 . test if our hadoop is set up  namenode , datanode1 , datanode2

     docker exec -it namenode bash 

     hdfs dfsadmin -report 


3.  If everything is OK, we can load the file from Kaggle, 'Full IMDb Dataset,' and import it into our PostgreSQL    database using a Python script that we will create .

load_data_to_db.py
URL = https://www.kaggle.com/api/v1/datasets/download/octopusteam/full-imdb-dataset
 
