# Part I. Prepared all required queries for later executions in Apache Cassandra.

# Import Python packages 
from cassandra.cluster import Cluster

# Queries: DROP TABLES
session_item_library_drop = 'DROP TABLE IF EXISTS session_item_library'
user_session_library_drop = 'DROP TABLE IF EXISTS user_session_library'
song_library_drop = 'DROP TABLE IF EXISTS song_library'

# Queries: CREATE TABLES (In NoSQL databases, model the data by thinking the queries first.)

# TO-DO: Query 1:  Extract the artist, song title and song's length in the music app history that was heard during \
# sessionId = 338, and itemInSession = 4
# Use sessionId & itemInSession as Primary Keys since each user will only have one pair of sessionId and itemInSession.
session_item_library_create = ("CREATE TABLE IF NOT EXISTS session_item_library \
                                (sessionId int, itemInSession int, artist text, song text, length float, \
                                PRIMARY KEY (sessionId, itemInSession));")

# TO-DO: Query 2: Extract the name of artist, song (sorted by itemInSession) and user (first and last name)\
# for userid = 10, sessionid = 182
# Use userId & sessionId as Primary Keys 
user_session_library_create = ("CREATE TABLE IF NOT EXISTS user_session_library \
                                (userId int, sessionId int, itemInSession int, song text, \
                                artist text, firstName text, lastName text, \
                                PRIMARY KEY ((userId, sessionId), itemInSession)) \
                                WITH CLUSTERING ORDER BY (itemInSession DESC);")

# TO-DO: Query 3: Extract every user name (first and last) in the music app history \
# who listened to the song 'All Hands Against His Own'
# Use song and userId as Primary Keys
song_library_create = ("CREATE TABLE IF NOT EXISTS song_library \
                        (song text, userId text, firstName text, lastName text, \
                        PRIMARY KEY (song, userId))")


# Queries: INSERT RECORDS
session_item_library_insert = "INSERT INTO session_item_library (sessionId,itemInSession,artist,song,length) \
                               VALUES (%s,%s,%s,%s,%s);"
user_session_library_insert = "INSERT INTO user_session_library (userId,sessionId,itemInSession,song,artist,firstName,lastName) \
                               VALUES (%s,%s,%s,%s,%s,%s,%s);"
song_library_insert = "INSERT INTO song_library (song,userId,firstName,lastName) \
                       VALUES (%s,%s,%s,%s);"

# QUERY LISTS
create_table_queries = [session_item_library_create,user_session_library_create,song_library_create]
drop_table_queries = [session_item_library_drop,user_session_library_drop,song_library_drop]