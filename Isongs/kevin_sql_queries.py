# DROP TABLES

time_table_drop = "DROP TABLE IF EXISTS time_table"
artist_table_drop = "DROP TABLE IF EXISTS artist_table"
user_table_drop = "DROP TABLE IF EXISTS user_table"
song_table_drop = "DROP TABLE IF EXISTS song_table"
songplay_table_drop = "DROP TABLE IF EXISTS songplay_table"

# CREATE TABLES
# Fact Table
songplay_table_create = ('CREATE TABLE IF NOT EXISTS songplay_table \
                        (songplay_id int, \
                        user_id int, \
                        song_id varchar, \
                        artist_id varchar, \
                        session_id int, \
                        start_time bigint, \
                        level varchar, \
                        location varchar, \
                        user_agent varchar);'
                        )
              
# Dimension Tables
# users - users in the app
user_table_create = ('CREATE TABLE IF NOT EXISTS user_table \
                    (user_id int, \
                    first_name varchar, \
                    last_name varchar, \
                    gender varchar, \
                    level varchar);'
                    )

# songs - songs in music database
song_table_create = ('CREATE TABLE IF NOT EXISTS song_table \
                    (song_id varchar, \
                    title varchar, \
                    artist_id varchar, \
                    year int, \
                    duration numeric);'
                    )

# artists - artists in music database
artist_table_create = ('CREATE TABLE IF NOT EXISTS artist_table \
                    (artist_id varchar, \
                    name varchar, \
                    location varchar, \
                    lattitude numeric, \
                    longitude numeric);'
                      )

# time - timestamps of records in songplays broken down into specific units
time_table_create = ('CREATE TABLE IF NOT EXISTS time_table \
                    (start_time bigint, \
                    hour int, \
                    day int, \
                    week int, \
                    month int, \
                    year int, \
                    weekday varchar);'
                    )

# INSERT RECORDS
songplay_table_insert = ('INSERT INTO songplay_table \
                        (songplay_id , \
                        start_time , \
                        user_id , \
                        level , \
                        song_id , \
                        artist_id , \
                        session_id , \
                        location , \
                        user_agent ) \
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);'
                        )

user_table_insert = ('INSERT INTO user_table \
                    (user_id , \
                    first_name , \
                    last_name , \
                    gender , \
                    level ) \
                    VALUES (%s,%s,%s,%s,%s);'
                    )

song_table_insert = (""" \
                    INSERT INTO song_table \
                    (song_id , \
                    title , \
                    artist_id , \
                    year , \
                    duration) \
                    VALUES (%s, %s,%s,%s, %s)
                    """)

artist_table_insert = ('INSERT INTO artist_table \
                    (artist_id, \
                    name, \
                    location, \
                    lattitude, \
                    longitude) \
                    VALUES (%s,%s,%s,%s,%s);'
                      )

time_table_insert = ('INSERT INTO time_table \
                    (start_time, \
                    hour, \
                    day, \
                    week, \
                    month, \
                    year, \
                    weekday) \
                    VALUES (%s,%s,%s,%s,%s,%s,%s);'
                    )

# FIND SONGS
song_select = ('SELECT song_table.song_id, artist_table.artist_id  FROM \
               song_table JOIN artist_table ON song_table.artist_id = artist_table.artist_id \
               WHERE song_table.title=%s and artist_table.name=%s and song_table.duration=%s'
              )

# QUERY LISTS
create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]