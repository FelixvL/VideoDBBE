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

def geefActeursOpAlleKenmerken(naamdeel,d,k,r,g):
    c, cr = geefVerbinding() # dictionary=True zorgt ervoor dat de resultaten als dict worden geretourneerd
    print(naamdeel,d,k,r,g)
    sqlstatement = "SELECT * FROM acteurs"
    sqlstatement += makeWhereClause(naamdeel,d,k,r,g)
    #cr.execute("SELECT * FROM acteurs WHERE Voornaam like '%"+naamdeel+"%' OR Achternaam like '%"+naamdeel+"%'")
    print(sqlstatement)
    cr.execute(sqlstatement)
    result = cr.fetchall()

    closeConnectionAndCursor(c, cr)

    return result

def makeWhereClause(n,d,k,r,g):
    returnstring = ""
    if n == "all" and d == "all" and k == "all" and r =="all" and g=="all":
        return ""
    else:
        returnstring += " WHERE"
        if n != "all":
            returnstring +=  " (Voornaam like '%"+n+"%' OR Achternaam like '%"+n+"%')"
        else:
            returnstring += " true"
        if g != "all":
            returnstring += " AND grootte = "+str(g)
        if d != "all":
            returnstring += " AND decennia = "+str(d)
        if k != "all":
            returnstring += " AND kleur = "+str(k)
        if r != "all":
            returnstring += " AND rating = "+str(r)
        return returnstring


#print(geefAlleActeurs())