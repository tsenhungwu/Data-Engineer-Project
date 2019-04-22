<p align="middle">
  <img width="450" height="380" src="https://github.com/tsenhungwu/Data-Engineer-Project/blob/master/Isongs/Images/Isongs.png" />
  
# Introduction
Compared with relational databases ([My PostgreSQL Data Modeling Project](https://github.com/tsenhungwu/Data-Engineer-Project/tree/master/Isongs)) and NoSQL databases ([My Apache Cassandra Data Modeling Project](https://github.com/tsenhungwu/Data-Engineer-Project/tree/master/Isongs_Apache_Cassandra)), Data Warehouses implemented and hosted on a cloud-based platform (Amazon Web Services or AWS) have severl advantages:

The advantages of using AWS to build cloud-based data warehouses:
  - Lower barrier to enter (we don't buy stuff but rent!)
  - May add or change as we need
  - Scalability and elasticity out of the box (add and remove resources)


Now, a music streaming platform has grown its user base and song database, and thus moving its data on the cloud might be a good choice. Currently, data resides in AWS S3 in a directory of JSON logs on user activity on the platform, as well as a directory with JSON metadata on it.

Again, using AWS, we can still answerer the specific questions proposed by the analytics team:  
  - What types of songs and artists are users listening to?
  - When is the most frequent time users logging into the app?
  - How long have users stayed on the app for each logging activity?

# Objectives
Throughout this project, I have achieved the following tasks:

- Built an ETL pipeline which extracts data from S3 bucket and stages data in Redshift.
- Optimized table design in Redshift to achieve a faster data ingestion process.
- Transformed data into a set of dimensional tables and fact table for continued analysis.


# Technology
<p align="middle">
  <img height="125" width="250" src="https://github.com/tsenhungwu/Data-Engineer-Project/blob/master/Isongs_AWS/Images/aws_redshift.png"/>
  <img height="200" width="300" src="https://github.com/tsenhungwu/Data-Engineer-Project/blob/master/Isongs_AWS/Images/aws_s3.png"/>
  <img height="150" width="250" src="https://github.com/tsenhungwu/Data-Engineer-Project/blob/master/Isongs_AWS/Images/aws_ec2.png"/>
  <img height="210" width="510" src="https://github.com/tsenhungwu/Data-Engineer-Project/blob/master/Isongs/Images/Python.png" />
</p>


# Raw Data Exploration
Data has been recorded between the dates November 1, 2018 and November 30, 2018.

Below is the screenshot of '2018-11-12-events.csv':

<img src="https://github.com/tsenhungwu/Data-Engineer-Project/blob/master/Isongs_Apache_Cassandra/Images/2018.11.12_event.png"/> 

I focused on specific attributes (11 items) compared with the original csv files:

<img src="https://github.com/tsenhungwu/Data-Engineer-Project/blob/master/Isongs_Apache_Cassandra/Images/image_event_datafile_new.jpg"/> 


# Key Methodology

## Schema Design
The special thing in schema designing in Apache Cassandra is to 'think queries first'.

In order to answer the proposed questions, following three tables were created: 

<p align="center">
  <b>1.session_item_library:</b>
  <br>Attain artist names, song titles and songs' duration in a music app history that was heard during specific sessions and number of items.<br>
  <br>Partition Keys: (sessionId, itemInSession) <br>
  <img src="https://github.com/tsenhungwu/Data-Engineer-Project/blob/master/Isongs_Apache_Cassandra/Images/session_item_library.png" />
</p>


<p align="center">
  <b>2.user_session_library:</b>
  <br>Obtain artist names, song titles and a user's name in a music app history that was heard by a particular user and session.<br>
  <br>Partition Keys: (userId, sessionId) / Clustering Column: itemInSession <br>
  <img src="https://github.com/tsenhungwu/Data-Engineer-Project/blob/master/Isongs_Apache_Cassandra/Images/user_session_library.png" />
</p>


<p align="center">
  <b>3.song_library:</b>
  <br>Obtain artist names, song titles and a user's name in a music app history that was heard by a particular user and session.<br>
  <br>Partition Keys: (song, userId) <br>
  <img src="https://github.com/tsenhungwu/Data-Engineer-Project/blob/master/Isongs_Apache_Cassandra/Images/song_library.png" />
</p>



# How does this project work?
To run the project successfully on a local machine, we need Apache Cassandra and Python3. 

**Step 1: The installation guidelines of both are provided: [Apache Cassandra](http://cassandra.apache.org/doc/latest/getting_started/installing.html) &  [Anaconda](https://www.datacamp.com/community/tutorials/installing-anaconda-mac-os-x).**

**Step 2: Outside the terminal, first download data.zip and unzip it.**

**Step 3: Inside the terminal, type followings line by line (if in a local machine, might need to initiate Apache Cassandra first):**
```
python kevin_create_event_csv.py (generate a narrow-down csv event file from all csv files)
python kevin_cassandra_creat_tables.py (create three tables in Apache Cassandra)
python kevin_cassandra_etl.py (insert corresponding records in three tables)
```
(Note that the keyspace setting will be different on your local machine.)

**Step 4: Finally, open kevin_cassandra_testing.ipynb to test the tables created in 'cassanrda_isongs' keyspace and to answer the questions.**

