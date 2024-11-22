
# Hadoop + PostgreSQL on Docker

This project sets up a Dockerized architecture including:
- A PostgreSQL database
- Hadoop HDFS with 1 NameNode and 2 DataNodes

1. Connect to the postgres database .

docker exec -it postgres psql -U admin -d mydb         


2 . test if our hadoop is set up