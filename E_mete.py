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
termo=0
baro=0
vele=0
pluvi=0

id_term=1
id_barometro=1
id_veleta=1
id_pluvi=1

periodo = 8000
def cambioPeriodo(val):
    global periodo
    periodo = val

def actualizarPeriodo():
    global periodo
    return periodo

# variables para mostrar en HTML del termometro
def variableTer():
    return termo

def promedioTer():
    global pro_ter
    pro_ter = 0
    pro_ter = baseDeDatos.consultaPromedioTermo()
    return pro_ter

def get_idTerm():
    global id_term
    return id_term

#Variables para mostrar en HTML del barometro
def variableBar():
    return baro

def promedioBar():
    global pro_bar
    pro_bar = 0
    pro_bar = baseDeDatos.consultaPromedioBaro()
    return pro_bar

def get_idBaro():
    global id_barometro
    return id_barometro

# variables para mostrar en HTML del pluviometro
def variablePluvi():
    return pluvi

def promedioPluvi():
    global pro_pluvi
    pro_pluvi = 0
    pro_pluvi = baseDeDatos.consultaPromedioPluvi()
    return pro_pluvi

def get_idPluvi():
    global id_pluvi
    return id_pluvi

# variables para mostrar en HTML del veleta
def variableVele():
    return vele

def promedioVele():
    global pro_vele
    pro_vele = 0
    pro_vele = baseDeDatos.consultaPromedioVeleta()
    return pro_vele

def get_idVele():
    global id_veleta
    return id_veleta

#Los siguientes 4 Def son para definir el comportamiento de musetreo de la estacion, a partir de 4 sensores
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
        global vele
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
        global pluvi
        #En mililitros
        pluvi=randint(100,1000)
        baseDeDatos.actualizarDatosPluvi(pluvi,id_pluvi)
        if id_pluvi == 10:
            id_pluvi = 1
        else:
            id_pluvi = id_pluvi + 1
