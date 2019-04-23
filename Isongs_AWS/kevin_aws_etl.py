import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries

# Function for loading (copying data) from S3 bucket into two staging tables
def load_staging_tables(cur, conn):
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()

# Function for inserting records from two staging tables into dimension and fact tables
def insert_tables(cur, conn):
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()

# Main function to connect to the Redshift, and to execute loading and inserting operations
def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()