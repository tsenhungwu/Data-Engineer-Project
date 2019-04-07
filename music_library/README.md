# Project Introduction
On a music streaming platform such as an app or a website, data have been transferred among different activities every day down to every millisecond.
To fully utilize the data and perform profound analysis on users' activities, it's extremely critical to design an architect or a data pipeline in an efficient way such that following analysis can be completed accordingly and iteratively.

The analytics team might be particularly interested in answering the following business questions: 
  - What types of songs and artists are users listening to?
  - When is the most frequent time users logging into the app?
  - How long have users stayed on the app for each logging activity? 

# Project Objective
Previously, data resided in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs.
Throughout this project, I have achieved the following tasks:

- Data modeling by normalizations with Postgres and built an ETL pipeline using Python. 
- Designed a Star Schema by combining fact and dimension tables for a particular analytic focus.
- Built an ETL pipeline which transfers data from JSON files in two local directories into tables in Postgres using Python and SQL queries.
- Optimized queries on song play analysis.

# Technology
<p align="middle">
  <img height="194" width="222" src="https://github.com/tsenhungwu/Data-Engineer-Project/blob/master/music_library/PostgreSQL.png" />
  <img height="203" width="601" src="https://github.com/tsenhungwu/Data-Engineer-Project/blob/master/music_library/Python.png" />
  
# Source Data
- Song dataset 

It is a subset of real data from the Million Song Dataset. (Reference: https://labrosa.ee.columbia.edu/millionsong/)

The files are partitioned by the first three letters of each song's track ID. 

For example, here are filepaths to two files in this dataset:
  
    song_data/A/B/C/TRABCEI128F424C983.json
  
    song_data/A/A/B/TRAABJL12903CDCF1A.json
  


# Raw Data Exploration
Data is mainly divided into two parts, Song dataset and Log dataset. 

Below are the screenshots of these two datasets:

- Take the 'TRAAABD128F429CF47.json' as an example: 
Each record contains metadata about a song and the artist of that song. 
<img height="78" width="1188" src="https://github.com/tsenhungwu/Data-Engineer-Project/blob/master/music_library/song_data.png" />



- Take the '2018-11-12-events.json' as an example: 
<img height="105" width="1502" src="https://github.com/tsenhungwu/Data-Engineer-Project/blob/master/music_library/log_data.png" />



# Methodology
## Star Schema Design 

