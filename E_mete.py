from random import randint
import baseDeDatos
import pprint
import time
import sys
import app
from flask import Flask
from flask import render_template
from flask import request

termo=0
def variableTer():
    return termo
def termometro():
        i = 1
        print("Se tomo valor del Termometro")
        global termo
        termo=randint(5,35)
        #baseDeDatos.actualizarDatos(termo,1)
        #time.sleep(10)
#Mide la presion atmosferica en mm
def barometro():
    i = 1
    while i != 100 :
        print("Se tomo valor del Barometro")
        baro=randint(8,68)
        baseDeDatos.actualizarDatos(baro,1)

#Indica la direccion del viento
def veleta():
    i = 1
    while i != 100 :
        print("Se tomo valor de la Veleta")
        vele=randint(0,360)
        baseDeDatos.actualizarDatos(vele,1)

#Mide la cantidad de agua caida
def pluvimetro():
    i = 1
    while i != 100 :
        print("Se tomo valor del Pluvimetro")
        #En mililitros
        pluvi=randint(100,1000)
        baseDeDatos.actualizarDatos(pluvi,1)


periodo = 10
def cambioPeriodo(valor):
    periodo = valor


#Funcion que toma todos los valores de forma secuencial cuando arranca el procesos
def TomarValores():
    i = 1
    while i != 100 :
        print("se cambio el valor de periodo a =")
        print(periodo)
        termometro()
        barometro()
        anenomtro()
        veleta()
        pluvimetro()
        heliografo()
        #Aca mandamos a la base de datos
