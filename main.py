# Equipo 1
# Lulú, Martha, Valeria y Lalo

import mysql.connector
import random

def insertarUsuario(name, password, age, gender):
	query = (f"INSERT INTO Users (name, password, age, gender) VALUES (%s, %s, %s, %s)")
	args = (name, password, age, gender)
	return [query, args]

def insertarNiveles(userID):
	ox = 90 + random.randrange(10)
	hr = 70 + random.randrange(40)
	day = 1 + random.randrange(28)
	month = 1 + random.randrange(12)
	date = str(2021) + '-' + str(month) + '-' + str(day)
	query = (f"INSERT INTO Levels (userID, oxygenSaturation, heartRate, date) VALUES (%s, %s, %s, %s)")
	
	args = (userID, ox, hr, date)
	# debajo de 95 ya es medio malo, abajo de 90 es baad
	return [query, args]

try:
	cnx = mysql.connector.connect(
		user = "root", 
		password = 'DEV.Lalongo1606', 
		host = "localhost", 
		database = 'TC1004B_Actividad',
	)

	cursor = cnx.cursor()

	usuarios = [
		['Phineas Flynn', 'Ferb ya se que vamos a hacer hoy', 11, 'H'],
		['Ferb Fletcher', 'nenanenanenanena', 11, 'H'],
		['Perry', 'dubidubiduba', 8, 'H'],
		['Pinky', 'chihuahua', 7, 'M'],
		['Pablo Marmol', 'ungabunga', 2000, 'H'],
		['Heinz Doofenshmirtz', 'malvadosyasociados', 40, 'H'],
	]
	# for u in usuarios:
	# 	usuario = insertarUsuario(u[0], u[1], u[2], u[3])
	# 	cursor.execute(usuario[0], usuario[1])
	# 	cnx.commit()

  	# para mandar parametros se pone %s
	query = (f"SELECT * FROM Users")
	cursor.execute(query)

	users = []

	print("USUARIOS: ")
	for result in cursor:
		print(result)
		users.append(result)
	for i in range(5000):
		for user in users:
			niveles = insertarNiveles(user[0])
			cursor.execute(niveles[0], niveles[1])
			cnx.commit()
			print(i, "Se agregaron los beios datos")

	query = (f"SELECT * FROM Levels")
	cursor.execute(query)

	print("NIVELES: ")
	for result in cursor:
		print(result)
except mysql.connector.Error as err:

	if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
		print("Something is wrong with your user name or password")
	elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
		print("Database does not exist")
	else:
		print(err)
	
# finally:
# 	cnx.close()