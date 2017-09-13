import psycopg2
import pprint
import sys


def actualizarDatosTermo(muestra,id_val):
     sql = """ UPDATE variables
                    SET var_ter = %s
                    WHERE variable_id = %s"""

     try:
         print('Conectando a PostgreSQL database para la carga de la tabla')
         conn = psycopg2.connect("host='localhost' dbname='practica1' user= 'postgres' password='castelli'")
         cur = conn.cursor()
         # execute the INSERT statement
         cur.execute(sql, (muestra,id_val))
         # Commit the changes to the database
         conn.commit()
         #Close communication with the PostgreSQL database
         cur.close()
     except (Exception, psycopg2.DatabaseError) as error:
            print(error)
     finally:
            if conn is not None:
                conn.close()

def actualizarDatosBaro(muestra,id_val):
     sql_baro = """ UPDATE variables
                    SET var_baro = %s
                    WHERE variable_id = %s"""

     try:
         print('Conectando a PostgreSQL database para la carga de la tabla')
         conn2 = psycopg2.connect("host='localhost' dbname='practica1' user= 'postgres' password='castelli'")
         cur2 = conn2.cursor()
         # execute the INSERT statement
         cur2.execute(sql_baro, (muestra,id_val))
         # Commit the changes to the database
         conn2.commit()
         #Close communication with the PostgreSQL database
         cur2.close()
     except (Exception, psycopg2.DatabaseError) as error:
            print(error)
     finally:
            if conn2 is not None:
                conn2.close()

def actualizarDatosVeleta(muestra,id_val):
     sql_veleta = """ UPDATE variables
                    SET var_vel = %s
                    WHERE variable_id = %s"""

     try:
         print('Conectando a PostgreSQL database para la carga de la tabla')
         conn3 = psycopg2.connect("host='localhost' dbname='practica1' user= 'postgres' password='castelli'")
         cur3 = conn3.cursor()
         # execute the INSERT statement
         cur3.execute(sql_veleta, (muestra,id_val))
         # Commit the changes to the database
         conn3.commit()
         #Close communication with the PostgreSQL database
         cur3.close()
     except (Exception, psycopg2.DatabaseError) as error:
            print(error)
     finally:
            if conn3 is not None:
                conn3.close()

def actualizarDatosPluvi(muestra,id_val):
     sql_pluvi = """ UPDATE variables
                    SET var_pluvi = %s
                    WHERE variable_id = %s"""

     try:
         print('Conectando a PostgreSQL database para la carga de la tabla')
         conn4 = psycopg2.connect("host='localhost' dbname='practica1' user= 'postgres' password='castelli'")
         cur4 = conn4.cursor()
         # execute the INSERT statement
         cur4.execute(sql_pluvi, (muestra,id_val))
         # Commit the changes to the database
         conn4.commit()
         #Close communication with the PostgreSQL database
         cur4.close()
     except (Exception, psycopg2.DatabaseError) as error:
            print(error)
     finally:
            if conn4 is not None:
                conn4.close()

def consultaPromedioTermo():
    sql_promedio1 = """SELECT AVG(variables.var_ter)
                       FROM variables"""

    try:
        print('Conectando a PostgreSQL database para la carga de la tabla')
        conn_pro = psycopg2.connect("host='localhost' dbname='practica1' user= 'postgres' password='castelli'")
        cur_pro = conn_pro.cursor()
        # execute the INSERT statement
        cur_pro.execute(sql_promedio1)
        promedio1 = cur_pro.fetchone()[0]
        # Commit the changes to the database
        conn_pro.commit()
        #Close communication with the PostgreSQL database
        cur_pro.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn_pro is not None:
            conn_pro.close()
    return "%.3f" %promedio1

def consultaPromedioBaro():
    sql_promedio2 = """SELECT AVG(variables.var_baro)
                       FROM variables"""
    try:
        print('Conectando a PostgreSQL database para la carga de la tabla')
        conn_pro2 = psycopg2.connect("host='localhost' dbname='practica1' user= 'postgres' password='castelli'")
        cur_pro2 = conn_pro2.cursor()
        # execute the INSERT statement
        cur_pro2.execute(sql_promedio2)
        # Commit the changes to the database
        promedio2 = cur_pro2.fetchone()[0]
        conn_pro2.commit()
        #Close communication with the PostgreSQL database
        cur_pro2.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn_pro2 is not None:
            conn_pro2.close()
    return "%.3f" %promedio2

def consultaPromedioVeleta():
    sql_promedio3 = """SELECT AVG(variables.var_vel)
                       FROM variables"""

    try:
        print('Conectando a PostgreSQL database para la carga de la tabla')
        conn_pro3 = psycopg2.connect("host='localhost' dbname='practica1' user= 'postgres' password='castelli'")
        cur_pro3 = conn_pro3.cursor()
        # execute the INSERT statement
        cur_pro3.execute(sql_promedio3)
        # Commit the changes to the database
        promedio3 = cur_pro3.fetchone()[0]
        conn_pro3.commit()
        #Close communication with the PostgreSQL database
        cur_pro3.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn_pro3 is not None:
            conn_pro3.close()
    return "%.3f" %promedio3

def consultaPromedioPluvi():
    sql_promedio4 = """SELECT AVG(variables.var_pluvi)
                       FROM variables"""
    try:
        print('Conectando a PostgreSQL database para la carga de la tabla')
        conn_pro4 = psycopg2.connect("host='localhost' dbname='practica1' user= 'postgres' password='castelli'")
        cur_pro4 = conn_pro4.cursor()
        # execute the INSERT statement
        cur_pro4.execute(sql_promedio4)
        # Commit the changes to the database
        promedio4 = cur_pro4.fetchone()[0]
        conn_pro4.commit()
        #Close communication with the PostgreSQL database
        cur_pro4.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn_pro4 is not None:
            conn_pro4.close()
    return "%.3f" %promedio4
