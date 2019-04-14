# Part II. Create keyspace and tables in Apache Cassandra.

# Import Python packages 
from cassandra.cluster import Cluster
from kevin_cassandra_queries import create_table_queries, drop_table_queries

def create_database():
    '''
    Outputs: Return the cluster object and connected session for executing queries in Apache Cassandra.
    '''
    # Connect to my local cluster.
    cluster = Cluster(['127.0.0.1'])

    # To establish connection and begin executing queries, need a session.
    session = cluster.connect()
    
    # Drop and create a keyspace.
    session.execute("DROP KEYSPACE IF EXISTS cassanrda_isongs")
    session.execute("CREATE KEYSPACE cassanrda_isongs \
                    WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1}")

    # Close the cluster and connection.
    cluster.shutdown()
    session.shutdown()

    # Connect to 'cassanrda_isongs' keyspace.
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect('cassanrda_isongs')

    return cluster, session

def drop_tables(session):
    '''
    Outputs (executions): Drop all tables in 'cassanrda_isongs' keyspace.
    '''
    for query in drop_table_queries:
        session.execute(query)

def create_tables(session):
    '''
    Outputs (executions): Create tables in 'cassanrda_isongs' keyspace.
    '''
    for query in create_table_queries:
        session.execute(query)

def main():
    cluster, session = create_database()
    drop_tables(session=session)
    create_tables(session=session)

if __name__ == "__main__":
    main()

