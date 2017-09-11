from random import uniform
from random import randint
import pprint
import sys
def termometro():
    print("Se tomo valor del Termometro")
    return randint(5,35)
#Mide la presion atmosferica en mm
def barometro():
    print("Se tomo valor del Barometro")
    return randint(8,68)
#Mide la velocidad del viento
def anenomtro():
    print("Se tomo valor del Anenometro")
    return uniform(2,6)
#Indica la direccion del viento
def veleta():
    print("Se tomo valor de la Veleta")
    return uniform(0,360)
#Mide la cantidad de agua caida
def pluvimetro():
    print("Se tomo valor del Pluvimetro")
    #En mililitros
    return uniform(100,1000)
#Mide las horas de luz solar
def heliografo():
    #print ("Se tomo valor del Heliografo")
    return randint(7,11)
#Funcion que toma todos los valores de forma secuencial cuando arranca el procesos
def TomarValores():
    termometro()
    barometro()
    anenomtro()
    veleta()
    pluvimetro()
    heliografo()
    #Aca mandamos a la base de datos
    
