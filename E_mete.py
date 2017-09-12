from random import randint
import baseDeDatos
import pprint
import time
import sys
import app
from flask import Flask
from flask import render_template
from flask import request
#hay que borrarla pero anda bien globalmente
id_term=1
id_barometro=1
id_veleta=1
id_pluvi=1


def variableTer():
    return termo

def termometro():

        print("Se tomo valor del Termometro")
        global termo
        global id_term
        termo=randint(5,35)
        baseDeDatos.actualizarDatosTermo(termo,id_term)
        if id_term == 10:
            id_term = 1
        else:
            id_term = id_term + 1


        #time.sleep(10)

#Mide la presion atmosferica en mm
def barometro():
        print("Se tomo valor del Barometro")
        global baro
        global id_barometro
        baro=randint(8,68)
        baseDeDatos.actualizarDatosBaro(baro,id_barometro)
        if id_barometro == 10:
            id_barometro = 1
        else:
            id_barometro = id_barometro + 1



#Indica la direccion del viento
def veleta():
        print("Se tomo valor de la Veleta")
        global id_veleta
        vele=randint(0,360)
        baseDeDatos.actualizarDatosVeleta(vele,id_veleta)
        if id_veleta == 10:
            id_veleta = 1
        else:
            id_veleta = id_veleta + 1

#Mide la cantidad de agua caida
def pluvimetro():
        print("Se tomo valor del Pluvimetro")
        global id_pluvi
        #En mililitros
        pluvi=randint(100,1000)
        baseDeDatos.actualizarDatosPluvi(pluvi,id_pluvi)
        if id_pluvi == 10:
            id_pluvi = 1
        else:
            id_pluvi = id_pluvi + 1
