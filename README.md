# Taller-de-proyecto-2
Se subiran los archivos de la materia taller de proyecto 2


# Instrucciones de uso Postgres

PASO 1
Abir terminal y colocar los siguientes comandos:

		sudo apt-get update
		sudo apt-get install postgresql postgresql-contrib
		pip install psycopg2 // si falla, buscar como instalar psycopg	

Luego tienen que configurarlo, asi que se colocar

		sudo -u postgres psql postgres

Eso va abrir la consola de postgres con el usurio "postgres" (no quieran cambiarlo por ahora que les va a traer problemas).

Finalmente, tienen que seguir la siguiente secuencia:
		
ATENCIÓN: NO DEJAR VACIO EL CAMPO DE CONTRASEÑA

		postgres=# \password postgres 
		Enter new password: 
		Enter it again: 
		postgres=# \q



PASO 2
Instalamos la interfaz apra manejar Postgres:

		sudo apt-get install pgadmin3

Al abrirla la interfaz no vana  tener nada conectado, asi que hagan click en el enchufe o boton conectar (arriba a la izquierda)
Completar de la siguiente manera:
		
		name: tallerDeProyecto2
		Host:localhost
		Port:5432
		Service:(vacio)
		MainenanceDB : postgres
		UserName : postgres
		passward : (la que gusten, pero la que ponga, fijense de entrar al .py y ponerle esta misma).
		
Presionar aceptar y listo, ya tienen el servidor creado, ahora entren hasta q les aparezca "Databases" y hagan click derecho y crear una base d datos nueva con el nombre practica1.

 Para poder seguir utilizando todo, sigan este tutorial:

		http://www.postgresqltutorial.com/postgresql-python/	

Tengan mucho cuidado con la identacion, no dejen espacios en blanco en python que aparentemente me trajo problemas.

