<p align="middle">
  <img width="450" height="380" src="https://github.com/tsenhungwu/Data-Engineer-Project/blob/master/Isongs/Images/Isongs.png" />
  
# Introduction
Compared with relational databases such as PostgreSQL ([My first PostgreSQL Data Modeling Project](https://github.com/tsenhungwu/Data-Engineer-Project/tree/master/Isongs)), NoSQL databases have advantages which can't be accomplished in relational databases.

The advantages of NoSQL databases include:
  - Deal with large amounts of data (big data)
  - Store different data type formats
  - High throughput
  - A flexible schema design
  - Horizontal scalability (linear scalability can be achieved if more nodes or clusters are provided)
  - High availability (fast reads)

    
On a music streaming platform such as an app or a website, data have been transferred among different activities every day down to every millisecond.
To fully utilize the data and perform profound analysis on users' activities, it's extremely critical to design an architect or a data pipeline in an efficient way such that following analysis can be completed accordingly and iteratively.

The analytics team might be particularly interested in answering the following questions (in an efficient way!): 
  - Attain artist names, song titles and songs' duration in a music app history that was heard during specific sessions and number of items.
  - Obtain artist names, song titles and a user's name in a music app history that was heard by a particular user and session.
  - Acquire users' names in a music app history who listened to a certain song.

# Objectives
Previously, there was no easy way to query the data to generate the results, since the data resided in a directory of CSV files on user activity on the app.

Throughout this project, I have achieved the following tasks:

- Data modeling with Apache Cassandra.
- Built an ETL pipeline which transfers data from csv files in local directories into tables in Apache Cassandra using Python and CQL queries (Cassandra Query Language).
- Formulated queries for answering specific questions (as I illustrated above).


# Technology
<p align="middle">
  <img height="270" width="300" src="https://github.com/tsenhungwu/Data-Engineer-Project/blob/master/Isongs_Apache_Cassandra/Images/Apache_Cassandra.jpg" />
  <img height="235" width="500" src="https://github.com/tsenhungwu/Data-Engineer-Project/blob/master/Isongs/Images/Python.png" />
</p>


# Raw Data Exploration
Data has been recorded between the dates November 1, 2018 and November 30, 2018.

Below is the screenshot of '2018-11-12-events.csv':

<img src="https://github.com/tsenhungwu/Data-Engineer-Project/blob/master/Isongs_Apache_Cassandra/Images/2018.11.12_event.png"/> 

I am more focus on specific attributes (11 items) compared with the original csv files:

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

Step 1: The installation guidelines for both are provided: [Apache Cassandra (http://cassandra.apache.org/doc/latest/getting_started/installing.html) &  [Anaconda](https://www.datacamp.com/community/tutorials/installing-anaconda-mac-os-x).

Step 2: Outside the terminal, first download data.zip.

Step 3: Inside the terminal, type followings line by line (if in a local machine, might need to initiate Apache Cassandra first):
```
python kevin_create_event_csv.py (generate a narrow-down csv event file from all csv files)
python kevin_cassandra_creat_tables.py (create three tables in Apache Cassandra)
python kevin_cassandra_etl.py (insert corresponding records in three tables)
```
(Note that the keyspace setting will be different on your local machine.)

Step 4: Finally, open kevin_cassandra_testing.ipynb to test the tables created in 'cassanrda_isongs' keyspace and to answer the questions.
