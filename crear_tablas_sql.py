"""
Creado por: Yohan Alfonso Hernandez
Fecha: 13-07-2023
Tema: conección de api y población de datos a database
"""
# Crear ambiente virual
# -python -m venv api-mysal
#instalar conecto a base de datos
#- mysql-connector-pytho
# install Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL
#- pip3 install sqlalchemy


# Create table 
import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='yohan',
    database='load_data_api'
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Define the SQL query to create a table
create_table_query = '''
    CREATE TABLE prueba_uno (
        ID INT PRIMARY KEY,
        Name VARCHAR(50),
        Age INT,
        Email VARCHAR(100)
    )'''

# Execute the create table query
cursor.execute(create_table_query)

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

