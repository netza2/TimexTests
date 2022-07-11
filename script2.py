import psycopg2
import datetime
from psycopg2 import Error

try:
    # Connection to the database in another container with default values
    connection = psycopg2.connect(user="postgres",
                                  password="password",
                                  host="172.17.0.2", # IP shown by the database container
                                  port="5432",
                                  database="postgres")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
       
    # Fetch result
    cursor.execute("SELECT * from personas where Nombre LIKE 'P%'")
    record = cursor.fetchall()
    print("Result ", record)
except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")