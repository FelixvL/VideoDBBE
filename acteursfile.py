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

def geefAlleActeurs():
    c, cr = geefVerbinding() # dictionary=True zorgt ervoor dat de resultaten als dict worden geretourneerd

    cr.execute("SELECT * FROM acteurs")
    result = cr.fetchall()

    closeConnectionAndCursor(c, cr)

    return result

def geefActeursOpNaam(naamdeel):
    c, cr = geefVerbinding() # dictionary=True zorgt ervoor dat de resultaten als dict worden geretourneerd

    cr.execute("SELECT * FROM acteurs WHERE Voornaam like '%"+naamdeel+"%' OR Achternaam like '%"+naamdeel+"%'")
    result = cr.fetchall()

    closeConnectionAndCursor(c, cr)

    return result
#print(geefAlleActeurs())