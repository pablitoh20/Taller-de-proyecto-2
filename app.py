# Lugar para poder los imports de python
import psycopg2
import pprint
import sys
from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

# app.route define la ruta donde se debe acceder

@app.route('/')
def connect():
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect("host='localhost' dbname='practica1' user= 'postgres' password='castelli'")
        # create a cursor
        cur = conn.cursor()
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
