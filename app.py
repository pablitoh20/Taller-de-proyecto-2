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
    hilo_temperatura = threading.Thread(target=E_mete.termometro)
    hilo_temperatura.start()
    hilo_barometro = threading.Thread(target=E_mete.barometro)
    hilo_barometro.start()
    hilo_veleta = threading.Thread(target=E_mete.veleta)
    hilo_veleta.start()
    hilo_pluvimetro =threading.Thread(target=E_mete.pluvimetro)
    hilo_pluvimetro.start()
    #actualizamos los id de las cosas para la base d datos
    return render_template('estacionInformacion.html',termo=E_mete.variableTer(),termo_promedio=4,termo_ultimaMuestra=E_mete.get_idTerm(),
                            humedad=E_mete.variablePluvi(), humedad_promedio=4, humedad_UltimaMuesta=E_mete.get_idPluvi(),
                            presion=E_mete.variableBar(), presion_promedio=4, presion_UltimaMuestra=E_mete.get_idBaro(),
                            viento=E_mete.variableVele(), viento_promedio=4, viento_UltimaMuestra=E_mete.get_idVele())

# Define la ruta y metodo con el que se debe llegar a este endpoint
@app.route('/estacionInformacion', methods = ['POST'])

#Definimos el comportamiento del formulario
def action_form():
    if request.method == 'POST':
        data = request.form
        if data["periodo"] == "1":
            #E_mete.cambioPeriodo(1)
            termo=1;
        elif data["periodo"] == "2":
            E_mete.cambioPeriodo(2)
        elif data["periodo"] == "5":
            E_mete.cambioPeriodo(5)
        elif data["periodo"] == "10":
            E_mete.cambioPeriodo(10)
        elif data["periodo"] == "30":
            E_mete.cambioPeriodo(30)
        elif data["periodo"] == "60":
            E_mete.cambioPeriodo(60)
        else:
            E_mete.cambioPeriodo(120) #es para completar, pero puede ir 0
        return render_template('estacionInformacion.html',termo=termo)

def actualizarPagina(variable):
        return render_template('estacionInformacion.html',variable=variable)
#Para realizar la conexion con la base de datos,configurar como indica el readm.md de git
def connect():
    conn = None
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
    #estMete = threading.Thread(target=E_mete.termometro)
    #info = threading.Thread(target)
    #connect()
    #estMete.start()
    #estMete.join()
    #print("Se termino el hilo")
    app.run(host='localhost', port=81)
    #E_mete.termometro()
