
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

docker exec -it postgres  psql -U postgres

 SELECT  title , genres, numvotes , releaseyear FROM  imdb WHERE releaseyear > 2000 LIMIT 5 ;

 
          title           |         genres         | numvotes | releaseyear 
--------------------------+------------------------+----------+-------------
 Everything's for You     | Documentary            |       17 |        2009
 Loading Ludwig           | NaN                    |        6 |        2022
 Idol Angel Yohkoso Yohko | Animation, Comedy      |      NaN |         NaN
 One Man War              | Action, Drama          |      NaN |         NaN
 The Wandering Soap Opera | Comedy, Drama, Fantasy |      371 |        2017


 #4. next step we extract data from the database , transform to csv and load it to hadoop

