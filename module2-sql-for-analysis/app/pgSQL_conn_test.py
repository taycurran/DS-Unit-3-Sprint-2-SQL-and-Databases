# This mod allows us to communicate with PostgreSQL
import psycopg2
# The Error class allows the app to understand errors in greater detail.
# This class returns an error message with an error code.
from psycopg2 import Error
# TODO - Write notes on dotenv and os modules
from dotenv import load_dotenv
import os

# Load Environment Variables
# Set Error Message to OPPS so its easy to identify
load_dotenv()
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

# We place our code in the try-except block to catch the database exceptions and errors
# that may occur during the process.

# Initial Test for Connection
try:
    # create a connection to our PostgreSQL database instance
    # the connect method accepts various enviornment variables as arguments
    connection = psycopg2.connect(user=DB_USER,
                                  password=DB_PASSWORD,
                                  host=DB_HOST,
                                  database=DB_NAME)
    # create cursor object allowing us to execute PostgreSQL 
    # command through Python source code.
    cursor = connection.cursor()
    # The connection object has an attribute to get connection properties
    # Print PostgresSQL Connection Properties
    print("CONNECTION PROPERTIES:", connection.get_dsn_parameters(), "\n")

    # Print PostgreSQL version
    # Cursor's excecute method allows us to execute a database query or operation
    # The excecute method thakes a SQL query as an argument.
    # Cursor's method fetchall, fetchone, or fetchmany() allow us retrieve query results
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    # closing DB connection
    # It is always good practice to close the cursor and connection object
    # once your work gets completed to avoid DB issues.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed.")
