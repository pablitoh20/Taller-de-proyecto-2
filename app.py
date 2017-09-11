# Lugar para poder los imports de python
# Importamos para tener varios hilos corriendo al mismo tiempo
#Importamos la funcion sleep para hacer dormir (va a marcar la frecuencia de muestreo en SEGUNDOS)
import psycopg2
import pprint
import sys
import E_mete
import baseDeDatos
import threading
from time import sleep
from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

# app.route define la ruta donde se debe acceder
@app.route('/')

#definimos cual es el inicio de la pagina
def index():
    return render_template('estacionInformacion.html')

# Define la ruta y metodo con el que se debe llegar a este endpoint
@app.route('/estacionInformacion', methods = ['POST'])

#Definimos el comportamiento del formulario
def action_form():
    if request.method == 'POST':
        data = request.form
        nombre = data["usuario"]
        passw= data["passw"]
        #Hay que modificar el nombre del HTML en caso de cambiarlo
    return render_template('respuesta.html', nombre=nombre, passw=passw)

#Para realizar la conexion con la base de datos,configurar como indica el readm.md de git
def connect():
    conn = None
    vendor_id = None
    try:
        print('Conectando a PostgreSQL database...')
        conn = psycopg2.connect("host='localhost' dbname='practica1' user= 'postgres' password='castelli'")
        # create a cursor
        cur = conn.cursor()
        # get the generated id back
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database conexion cerrada.')

if __name__ == '__main__':
    #Creamos la tabla de la base de datos
    #baseDeDatos.creacionTabla()
    #baseDeDatos.insertarDatos([(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,)])
    #Cargamos dicha tabla con valores en 0
    estMete = threading.Thread(target=E_mete.TomarValores)
    #info = threading.Thread(target)
    #connect()
    estMete.start()
    estMete.join()
    print("Se termino el hilo")
    app.run(host='localhost', port=80)
