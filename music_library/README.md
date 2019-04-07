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
  <img height="200" width="225" src="https://github.com/tsenhungwu/Data-Engineer-Project/blob/master/music_library/PostgreSQL.png" />
  <img height="190" width="500" src="https://github.com/tsenhungwu/Data-Engineer-Project/blob/master/music_library/Python.png" />

# Raw Data Exploration
Data is mainly divided into two parts, Song Dataset and Log Dataset.
Below are the screenshots of these two datasets:

<img height="200" width="300" src="https://github.com/tsenhungwu/Data-Engineer-Project/blob/master/music_library/song_data.png" />

<img height="200" width="225" src="https://github.com/tsenhungwu/Data-Engineer-Project/blob/master/music_library/log_data.png" />



# Methodology
## Star Schema Design 

