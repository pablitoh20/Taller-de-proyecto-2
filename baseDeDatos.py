import psycopg2
import pprint
import sys

#Realiza la conexion a la base de datos para realziar la prueba de conexion la pimera vez
def connect():
    conn = None
    try:
        print('Conectando a PostgreSQL database para la carga de la tabla')
        conn = psycopg2.connect("host='localhost' dbname='practica1' user= 'postgres' password='castelli'")
        # create a cursor
        cur = conn.cursor()
        # cerrar cursor
        cur.close()
        # commit the changes
        conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database conexion cerrada.')

#Creacion de las tablas de la base de datos, inicializado todo en 0 o ull o lo que corresponda
def creacionTabla():
    commands = (
        """
        CREATE TABLE variables (
            variable_id SERIAL PRIMARY KEY,
            var_ter VARCHAR(5) NOT NULL,
            var_baro VARCHAR(5) NOT NULL,
            var_aneno VARCHAR(5) NOT NULL,
            var_vel VARCHAR(5) NOT NULL,
            var_pluvi VARCHAR(5) NOT NULL,
            var_heli VARCHAR(5) NOT NULL
        );
        """
        )
    conn = None
    try:
        # read the connection parameters
        print('Conectando a PostgreSQL database para la carga de la tabla')
        conn = psycopg2.connect("host='localhost' dbname='practica1' user= 'postgres' password='castelli'")
        # create a cursor
        cur = conn.cursor()
        # create table one by one
        cur.execute(commands)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

#Poner los primeros 10 valores a la tabla para que funcione con el inciso de la practica.
def insertarDatos(var_list):
    sql = "INSERT INTO variables(var_ter) VALUES(%s)"
    conn = None
    try:
        print('Conectando a PostgreSQL database para la carga de la tabla')
        conn = psycopg2.connect("host='localhost' dbname='practica1' user= 'postgres' password='castelli'")
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql,var_list)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
