# Queries: DROP TABLES

time_table_drop = "DROP TABLE IF EXISTS time_table"
artist_table_drop = "DROP TABLE IF EXISTS artist_table"
user_table_drop = "DROP TABLE IF EXISTS user_table"
song_table_drop = "DROP TABLE IF EXISTS song_table"
songplay_table_drop = "DROP TABLE IF EXISTS songplay_table"

# Queries: CREATE TABLES
# Fact Table
# songplay_id is an auto-increment primary key. Each row will be uniquely identified by songplay_id.
# data type of start_time is bigint since the number is 8 bytes.
songplay_table_create = ('CREATE TABLE IF NOT EXISTS songplay_table \
                        (songplay_id SERIAL PRIMARY KEY, \
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
                    (user_id int PRIMARY KEY, \
                    first_name varchar, \
                    last_name varchar, \
                    gender varchar, \
                    level varchar);'
                    )

# songs - songs in music database
song_table_create = ('CREATE TABLE IF NOT EXISTS song_table \
                    (song_id varchar PRIMARY KEY, \
                    title varchar, \
                    artist_id varchar, \
                    year int, \
                    duration numeric);'
                    )

# artists - artists in music database
artist_table_create = ('CREATE TABLE IF NOT EXISTS artist_table \
                    (artist_id varchar PRIMARY KEY, \
                    name varchar, \
                    location varchar, \
                    lattitude numeric, \
                    longitude numeric);'
                    )

# time - timestamps of records in songplays broken down into specific units
time_table_create = ('CREATE TABLE IF NOT EXISTS time_table \
                    (start_time bigint PRIMARY KEY, \
                    hour int, \
                    day int, \
                    week int, \
                    month int, \
                    year int, \
                    weekday varchar);'
                    )

# Queries: INSERT RECORDS
songplay_table_insert = ('INSERT INTO songplay_table \
                        (user_id, \
                        song_id, \
                        artist_id, \
                        session_id, \
                        start_time, \
                        level, \
                        location, \
                        user_agent) \
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s);'
                        )
# There might be duplicate users. Use upset operation to avoid this scenario on user_id.
user_table_insert = ('INSERT INTO user_table \
                    (user_id , \
                    first_name , \
                    last_name , \
                    gender , \
                    level ) \
                    VALUES (%s,%s,%s,%s,%s) \
                    ON CONFLICT (user_id) DO UPDATE SET level = excluded.level;'
                    )

song_table_insert = ('INSERT INTO song_table \
                    (song_id, \
                    title, \
                    artist_id, \
                    year, \
                    duration) \
                    VALUES (%s, %s,%s,%s, %s);'
                    )

# There might be duplicate artists. Use upset operation to avoid this scenario on artist_id.
artist_table_insert = ('INSERT INTO artist_table \
                        (artist_id, \
                        name, \
                        location, \
                        lattitude, \
                        longitude) \
                        VALUES (%s,%s,%s,%s,%s) \
                        ON CONFLICT (artist_id) DO NOTHING;'
                        )

# There might be duplicate times. Use upset operation to avoid this scenario on start_time.
time_table_insert = ('INSERT INTO time_table \
                    (start_time, \
                    hour, \
                    day, \
                    week, \
                    month, \
                    year, \
                    weekday) \
                    VALUES (%s,%s,%s,%s,%s,%s,%s) \
                    ON CONFLICT (start_time) DO NOTHING;'
                    )

# Queries: FIND SONGS
# By joining two tables, artist_table and song_table together, attain the corresponding song_id and artist_id given 
# the constraints from title, name, and duration.
song_select = ('SELECT song_table.song_id, artist_table.artist_id  \
               FROM song_table JOIN artist_table \
               ON song_table.artist_id = artist_table.artist_id \
               WHERE song_table.title=%s and artist_table.name=%s and song_table.duration=%s'
              )

# QUERY LISTS
create_table_queries = [artist_table_create, user_table_create, song_table_create, time_table_create, songplay_table_create]
drop_table_queries = [artist_table_drop, user_table_drop, song_table_drop, time_table_drop, songplay_table_drop]