import mysql.connector

def geefVerbinding():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="filmdb"
    )
    return connection, connection.cursor(dictionary=True)

def closeConnectionAndCursor(connection, cursor):
    cursor.close()
    connection.close()

def volgendvideomomentopvragen():

    c, cr = geefVerbinding() # dictionary=True zorgt ervoor dat de resultaten als dict worden geretourneerd

    cr.execute("SELECT * FROM films WHERE id = 1")
    result = cr.fetchall()

    closeConnectionAndCursor(c, cr)

    return result[0]

def videomomentopslaan(v,a,t):
    c, cr = geefVerbinding()
    update_statement = "INSERT INTO `film_acteur_momenten` (`film_id`, `acteur_id`, `start_tijd`) VALUES (%s, %s, %s);"
    values = (v,a,t)

    t = cr.execute(update_statement, values)

    c.commit()

    return "opgeslagen"


print(volgendvideomomentopvragen())
    