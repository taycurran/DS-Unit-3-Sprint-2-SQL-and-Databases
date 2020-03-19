import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv
import os

# Load Environment Variables
load_dotenv()
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

try:
    connection = psycopg2.connect(user=DB_USER,
                                  password=DB_PASSWORD,
                                  host=DB_HOST,
                                  database=DB_NAME)
    cursor = connection.cursor()

    create_table_Q = """
                     CREATE TABLE IF NOT EXISTS passengers (
                        id SERIAL PRIMARY KEY,
                        survived INT,
                        pclass INT,
                        name VARCHAR(100),
                        sex VARCHAR(10),
                        age INT,
                        sib_spouce_count INT,
                        parent_child_count INT,
                        fare float8
                     );
                     """

    cursor.execute(create_table_Q)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

except (Exception, psycopg2.DatabaseError) as error:
    print ("Error while creating PostgreSQL table", error)
finally:
    # Closing DB connection
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


    