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

def kentoe(cat,waarde,fid):
    c, cr = geefVerbinding() # dictionary=True zorgt ervoor dat de resultaten als dict worden geretourneerd

    print("UPDATE acteurs SET "+letternaarcategorei(cat)+" = "+waarde+" WHERE id = "+fid+"")

    update_statement = "UPDATE acteurs SET "+letternaarcategorei(cat)+" = %s WHERE id = %s"

    values = (waarde, fid)

    t = cr.execute(update_statement, values)
    print(t)
    c.commit()
    closeConnectionAndCursor(c, cr)

    return '{"hh":"hh"}'
def letternaarcategorei(letter):
    categorie = ["Grootte","Rating","Decennia","Kleur"]
    if letter == "g":
        return categorie[0]
    if letter == "r":
        return categorie[1]
    if letter == "d":
        return categorie[2]
    if letter == "k":
        return categorie[3]

def geefActeursOpNaam(naamdeel):
    c, cr = geefVerbinding() # dictionary=True zorgt ervoor dat de resultaten als dict worden geretourneerd

    cr.execute("SELECT * FROM acteurs WHERE (Voornaam like '%"+n+"%' OR Achternaam like '%"+n+"%' OR AfbeeldingURL like '%"+n+"%')")
    result = cr.fetchall()

    closeConnectionAndCursor(c, cr)

    return result

def zoeknullopcategorie(cat):
    c, cr = geefVerbinding() # dictionary=True zorgt ervoor dat de resultaten als dict worden geretourneerd
    kolom = ""
    if(cat == "g"):
        kolom = "Grootte"
    if(cat == "k"):
        kolom = "Kleur"
    if(cat == "r"):
        kolom = "Rating"
    if(cat == "d"):
        kolom = "Decennia"
    cr.execute("SELECT * FROM acteurs WHERE "+kolom+" is null")
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
            returnstring +=  " (Voornaam like '%"+n+"%' OR Achternaam like '%"+n+"%' OR AfbeeldingURL like '%"+n+"%')"
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