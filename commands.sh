#!/bin/sh
docker run --name postg -e POSTGRES_PASSWORD=password --rm --network bridge postgres
docker run -it --rm -v /home/netza/Documents/Jupyter/TimexTest:/home/work --network bridge mhoush/psycopg2
#>>>import os
#>>>os.chdir('/home/work')
#>>>import script1

#Table created successfully in PostgreSQL
#1 Record inserted successfully
#1 Record inserted successfully
#1 Record inserted successfully
#1 Record inserted successfully
#Result  [(1, 'Pedro', 'Mola', '19791011', datetime.datetime(2022, 7, 11, 15, 13, 46, 581505)), (2, 'Pablo', 'Videgaray', '19750105', datetime.datetime(2022, 7, 11, 15, 13, 46, 584194)), (3, 'Sonia', 'Lopez', '19850306', datetime.datetime(2022, 7, 11, 15, 13, 46, 586612)), (4, 'Alex', 'Perez', '19800708', datetime.datetime(2022, 7, 11, 15, 13, 46, 589108))]
#PostgreSQL connection is closed

#>>>import script2

#Result  [(1, 'Pedro', 'Mola', '19791011', datetime.datetime(2022, 7, 11, 15, 13, 46, 581505)), (2, 'Pablo', 'Videgaray', '19750105', datetime.datetime(2022, 7, 11, 15, 13, 46, 584194))]
#PostgreSQL connection is closed

