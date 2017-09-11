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


#definimos cual es el fomrulario de inicio de la pagina
def index():
    return render_template('form.html')
# Define la ruta y metodo con el que se debe llegar a este endpoint
@app.route('/form', methods = ['POST'])

#Definimos el comportamiento del formulario
def action_form():

    if request.method == 'POST':
        data = request.form
        nombre = data["usuario"]
        passw= data["passw"]
    return render_template('respuesta.html', nombre=nombre, passw=passw)
# Para realizar la conexion con la base de datos,configurar como indica el readm.md de git
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
    app.run(host='localhost', port=80)
