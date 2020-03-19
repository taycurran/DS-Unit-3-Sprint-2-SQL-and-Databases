import psycopg2
from dotenv import load_dotenv
import os

# Load Environment Variables
load_dotenv()
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

# Initial Test for Connection
try:
    connection = psycopg2.connect(user=DB_USER,
                                  password=DB_PASSWORD,
                                  host=DB_HOST,
                                  database=DB_NAME)
    cursor = connection.cursor()
    # Print PostgresSQL Connection Properties
    print("CONNECTION PROPERTIES:", connection.get_dsn_parameters(), "\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    # closing DB connection
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed.")
