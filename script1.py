import psycopg2
import datetime
from psycopg2 import Error

try:
    # Connection to the database in another container with default values
    connection = psycopg2.connect(user="postgres",
                                  password="password",
                                  host="172.17.0.2",
                                  port="5432", # IP shown by the database container
                                  database="postgres")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # SQL query to create a new table
    create_table_query = '''CREATE TABLE personas
          (IDREGISTRO INT PRIMARY KEY     NOT NULL,
          NOMBRE           TEXT    NOT NULL,
          APELLIDOS           TEXT    NOT NULL,
          FECHANACIMIENTO         TEXT,
          FECHAREGISTROENSISTEMA TIMESTAMP); '''
    # Execute a command: this creates a new table
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")
    
    # Registro 1
    insert_query = """ INSERT INTO personas (IdRegistro, Nombre, Apellidos, FechaNacimiento, FechaRegistroEnSistema) VALUES (1, 'Pedro', 'Mola', '19791011', %s) """
    #timestamp = (datetime.datetime.now(),)
    
    cursor.execute(insert_query, (datetime.datetime.now(),))
    connection.commit()
    print("1 Record inserted successfully")
    # Registro 2
    insert_query = """ INSERT INTO personas (IdRegistro, Nombre, Apellidos, FechaNacimiento, FechaRegistroEnSistema) VALUES (2, 'Pablo', 'Videgaray', '19750105', %s) """
    #timestamp = (datetime.datetime.now(),)
    
    cursor.execute(insert_query, (datetime.datetime.now(),))
    connection.commit()
    print("1 Record inserted successfully")
    # Registro 3
    insert_query = """ INSERT INTO personas (IdRegistro, Nombre, Apellidos, FechaNacimiento, FechaRegistroEnSistema) VALUES (3, 'Sonia', 'Lopez', '19850306', %s) """
    #timestamp = (datetime.datetime.now(),)
    
    cursor.execute(insert_query, (datetime.datetime.now(),))
    connection.commit()
    print("1 Record inserted successfully")
    # Registro 4
    insert_query = """ INSERT INTO personas (IdRegistro, Nombre, Apellidos, FechaNacimiento, FechaRegistroEnSistema) VALUES (4, 'Alex', 'Perez', '19800708', %s) """
    #timestamp = (datetime.datetime.now(),)
    
    cursor.execute(insert_query, (datetime.datetime.now(),))
    connection.commit()
    print("1 Record inserted successfully")
    
    # Fetch result
    cursor.execute("SELECT * from personas")
    record = cursor.fetchall()
    print("Result ", record)
except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")