import mysql.connector
import datetime

def login():
    """
    Verifies username and password.
    Returns userID.
    """
    u_name = 1
    u_password = 1

    # get username
    while(u_name):
        userName = input("Ingresa tu usuario: ")
        query = (f"SELECT * FROM Users WHERE name=%s")
        args = (userName,)
        cursor.execute(query, args)
        info = cursor.fetchall()[0]
        if len(info) > 0:
            u_name = 0

            # get password
            while(u_password):
                password = input("Ingresa tu contraseña: ")
                if info[2] == password:
                    u_password = 0
                else:
                    print("Contraseña incorrecta, vuelve a intentarlo")
                    
        else:
            print("Usuario incorrecto, vuelve a intentarlo")
    
    return info[0]

def insert_into_database(heartRate, oxygenSaturation):
    query = (f"INSERT INTO Levels(userID, heartRate, oxygenSaturation, date) VALUES(%s, %s, %s, %s)")
    today = str(datetime.datetime.now())
    args = (userID, heartRate, oxygenSaturation, today)
    cursor.execute(query,args)
    cnx.commit()

try:
    cnx = mysql.connector.connect(
        user = "root", 
        password = "mac_15_db", 
        port = "3306",
        database = 'reto_iot'
    )

    cursor = cnx.cursor(buffered=True)

    userID = login()
    print(userID)
    

except mysql.connector.Error as err:
    if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

finally:
    cnx.close()