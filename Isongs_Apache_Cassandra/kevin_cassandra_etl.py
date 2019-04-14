# Part III. Inserting records into Apache Cassandra tables.

# Import Python packages 
import csv
from cassandra.cluster import Cluster
from kevin_cassandra_queries import *

# Insert functions
def process_session_item_library(session,filepath):
        '''
        session: a connector to the keyspace in Apache Cassandra.
        filepath: a csv file path.
        Outputs (executions): Insert records into session_item_library table.
        '''
        file = filepath
        # Open a csv file.
        with open(file, encoding = 'utf8') as f:
                csvreader = csv.reader(f)
                # Skip the header.
                next(csvreader)
                # Insert records into the session_item_library table.
                for line in csvreader:
                        session.execute(session_item_library_insert, \
                                (int(line[8]), int(line[3]), line[0], line[9], float(line[5])))

def process_user_session_library(session,filepath):
        '''
        session: a connector to the keyspace in Apache Cassandra.
        filepath: a csv file path.
        Outputs (executions): Insert records into user_session_library table.
        '''
        file = filepath
        # Open a csv file.
        with open(file, encoding = 'utf8') as f:
                csvreader = csv.reader(f)
                # Skip the header.
                next(csvreader)
                # Insert records into the user_session_library table.
                for line in csvreader:
                        session.execute(user_session_library_insert, \
                                (int(line[10]), int(line[8]), int(line[3]), line[0], line[9], line[1], line[4]))

def process_song_library(session,filepath):
        '''
        session: a connector to the keyspace in Apache Cassandra.
        filepath: a csv file path.
        Outputs (executions): Insert records into process_song_library table.
        '''
        file = filepath
        # Open a csv file.
        with open(file, encoding = 'utf8') as f:
                csvreader = csv.reader(f)
                # Skip the header.
                next(csvreader)
                # Insert records into the process_song_library table.
                for line in csvreader:
                        session.execute(song_library_insert, (line[9], line[-1], line[1], line[4]))

# Process function lists (can be expanded later if more operations are needed).
process_functions = [process_session_item_library,process_user_session_library,process_song_library]

def main():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect('cassanrda_isongs')
    total_functions = len(process_functions)
    for i in range(total_functions):
        print('Inserting data into {}/{} tables.'.format(i+1,total_functions))
        process_functions[i](session=session,filepath='event_datafile_new.csv')

    cluster.shutdown()
    session.shutdown()

if __name__ == "__main__":
    main()

