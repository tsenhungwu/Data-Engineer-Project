import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries

# Function for dropping all tables if existed 
def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

# Function for creating all tables if not existed
def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

# Main function to connect to the Redshift, and to execute dropping and creating table operations
def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()