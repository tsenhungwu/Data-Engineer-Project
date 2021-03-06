<p align="middle">
  <img width="450" height="380" src="https://github.com/tsenhungwu/Data-Engineer-Project/blob/master/Isongs/Images/Isongs.png" />
  
# Introduction
On a music streaming platform such as an app or a website, data have been transferred among different activities every day down to every millisecond.
To fully utilize the data and perform profound analysis on users' activities, it's extremely critical to design an architect or a data pipeline in an efficient way such that following analysis can be completed accordingly and iteratively.

The analytics team might be particularly interested in answering the following business questions: 
  - What types of songs and artists are users listening to?
  - When is the most frequent time users logging into the app? 
  - How long have users stayed on the app for each logging activity?

# Objectives
Previously, data resided in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs.
Throughout this project, I have achieved the following tasks:

- Data modeling with PostgreSQL.
- Designed a Star Schema by combining fact and dimension tables for a particular analytic focus.
- Built an ETL pipeline which transfers data from JSON files in two local directories into tables in PostgreSQL using Python and SQL queries.
- Optimized queries on song play analysis.

# Technology
<p align="middle">
  <img src="https://github.com/tsenhungwu/Data-Engineer-Project/blob/master/Isongs/Images/PostgreSQL.png" />
  <img src="https://github.com/tsenhungwu/Data-Engineer-Project/blob/master/Isongs/Images/Python.png" />
  
# Data Source
- Song dataset

It is a subset of real data from [the Million Song Dataset](https://labrosa.ee.columbia.edu/millionsong/). 

The files are partitioned by the first three letters of each song's track ID. 

For example, here are file paths to two files in this dataset:
  
    song_data/A/B/C/TRABCEI128F424C983.json
    song_data/A/A/B/TRAABJL12903CDCF1A.json
  
- Log dataset

The second dataset consists of log files in JSON format generated by [the event simulator](https://github.com/Interana/eventsim) based on the songs in the dataset above. 

These simulate app activity logs from a music streaming app based on specified configurations. 

The log files in the dataset I worked with are partitioned by year and month. 

For example, here are file paths to two files in this dataset:

    log_data/2018/11/2018-11-12-events.json
    log_data/2018/11/2018-11-13-events.json


# Raw Data Exploration
Data is mainly divided into two parts, Song dataset and Log dataset. 

Below are the screenshots of these two datasets:

- Take the 'TRAAABD128F429CF47.json' as an example: 
Each record contains metadata about a song and the artist of that song. 
<img height="78" width="1188" src="https://github.com/tsenhungwu/Data-Engineer-Project/blob/master/Isongs/Images/song_data.png" />



- Take the '2018-11-12-events.json' as an example: 

<img src="https://github.com/tsenhungwu/Data-Engineer-Project/blob/master/Isongs/Images/log_data1.png" height="104" width="971"/> 
<img src="https://github.com/tsenhungwu/Data-Engineer-Project/blob/master/Isongs/Images/log_data2.png" height="108" width="227"/> 


# Key Methodology

## Star Schema Design - ERD
<p align="middle">
<img height="355" width="634" src="https://github.com/tsenhungwu/Data-Engineer-Project/blob/master/Isongs/Images/ERD.png" />


# How does this project work?
To run the project successfully on a local machine, we need PostgreSQL and Python3. 

The installation guidelines for both are provided: [PostgreSQL](https://www.codementor.io/engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb) &  [Anaconda](https://www.datacamp.com/community/tutorials/installing-anaconda-mac-os-x).


Inside the terminal, type followings line by line:
```
python kevin_create_tables.py
python kevin_etl.py
```
(Note that the database setting will be different on your local machine.)

Finally, open kevin_testing.ipynb to test the tables created in isongs database.
