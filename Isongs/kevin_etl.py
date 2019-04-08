import os
import glob
import psycopg2
import pandas as pd
import numpy as np
from kevin_sql_queries import *


def process_song_file(cur, filepath):
    '''
    cur: a cursor or a driver to send queries to a database.
    filepath: a file path of a JSON file.
    Outputs: execute queries of inserting data into the song_table and artist_table.
    '''
    # open song file
    df = pd.read_json(filepath, lines=True)

    # get attributes of song_table 
    song_data = df[['song_id','title','artist_id','year','duration']].values[0].tolist()

    # insert song record into song_table
    cur.execute(song_table_insert, song_data)
    
    # get attributes of artist_table
    artist_data = df[['artist_id','artist_name','artist_location','artist_latitude','artist_longitude']].values[0].tolist()
    
    # insert artist record into artist_table
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    '''
    cur: a cursor or a driver to send queries to a database.
    filepath: a file path of a JSON file.
    Outputs: 
    '''

    # open log file
    df = pd.read_json(filepath, lines=True)
    
    # filter records by 'NextSong' action
    df = df[df['page'] == 'NextSong']

    # time_table 
    # convert timestamp column 'ts' to a datetime type
    df_log = df['ts']
    t = pd.to_datetime(df_log)
    
    # attain other time attributes
    time_data = (df_log,
                 t.dt.hour.values, t.dt.day.values, t.dt.week.values, 
                 t.dt.month.values, t.dt.year.values, t.dt.weekday.values)
    column_labels = ('start_time','hour','day','week','month','year','weekday')
    time_df = pd.DataFrame({column_labels[0]:time_data[0],
                            column_labels[1]:time_data[1],
                            column_labels[2]:time_data[2],
                            column_labels[3]:time_data[3],
                            column_labels[4]:time_data[4],
                            column_labels[5]:time_data[5],
                            column_labels[6]:time_data[6]
                           })
    # insert time data records into time_table
    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # user_table
    # attain attributes of user_table
    user_df = df[['userId','firstName','lastName','gender','level']]
    
    # insert user records into user_table
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # songplay_table
    # insert songplay records
    for index, row in df.iterrows():
        
        # According to song, artist, and length from log file, 
        # get songid and artistid from song_table and artist_table.
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        # If results are not None, meaning we are able to retrieve the records from song_table and artist_table.
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record into songplay_table
        songplay_data = (row.userId,songid,artistid,row.sessionId,row.ts,row.level,row.location,row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    '''
    cur: a cursor or a driver to send queries to a database.
    conn: a connection to a database.
    filepath: a file path of a JSON file.
    func: a function of inserting data into a table.
    '''
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=isongs user=wuchenhong")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()