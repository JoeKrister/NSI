import csv, sqlite3

con = sqlite3.connect('collection.db')
liste_types = set()
collections=[]
with open('collection_piece_29.csv', newline='', encoding='utf8') as csvfile:
    reader = csv.reader(csvfile)
    curseur=con.cursor()
    curseur.execute("""DROP TABLE IF EXISTS collection""")
    curseur.execute("""CREATE TABLE IF NOT EXISTS collection
    (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    nom VARCHAR(40),
    nb_exemplaire SMALLINT,
    emetteur VARCHAR(40),
    type VARCHAR(40),
    date SMALLINT,
    devise VARCHAR(40),
    composition VARCHAR(20),
    poids REAL,
    diametre REAL,
    epaisseur REAL,
    forme VARCHAR(20),
    demonetise CHAR(3),
    indice_rarete SMALLINT,
    avers TEXT,
    envers TEXT;)
    """)
    for line in list(reader)[1:] :
        if " "in line[1] :
            splited = line[1].split(" ")
            print(splited)
            for t in splited[1: ] :
                
                if len(t)>1 and t in splited[0] :
                    newl = splited[0].split(t)[-1]
                    name = newl+" "+" ".join(splited[1:])
                    imgname = "-".join(name.split(" "))
        else :
                name= line[1]
                imgname= line[1]
        type1, type2 = line[3].strip(), line[4].strip()
        if type1 != "" :
            liste_types =liste_types | set([type1])
        if type2 != "" :
            liste_types=liste_types | set([type2])
        
        collections.append([name.lower(),imgname.lower(), line[2], type1, type2, *line[5:]])
con.commit()
con.close()
con = sqlite3.connect('collection.db')
curseur=con.cursor()
for typ in liste_types :
    req = f"""INSERT INTO Type(nom_type) VALUES (?);"""
    curseur.execute(req, [typ])
con.commit()
con.close()
con = sqlite3.connect('collection.db')
curseur=con.cursor()



for pok in collections :
    type1=pok[3]
    type2=pok[4]
    if type1 !="" :
        req=f"""SELECT id FROM Type WHERE nom_type='{type1}';"""
        curseur.execute(req)
        reponse= curseur.fetchone()
        id_type1=reponse[0]
    else :
        id_type1 = None
    if type2 !="" :
        req=f"""SELECT id FROM Type WHERE nom_type='{type2}';"""
        curseur.execute(req)
        reponse= curseur.fetchone()
        id_type2=reponse[0]
    else :
        id_type2 = None
        
    
    con.commit()
con.close()

   
req = f""" INSERT INTO collection (id, nom, nb_exemplaire, emetteur, type, date, devise, composition, poids, diametre, epaisseur, forme, demonetise, indice_rarete, avers, envers    ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"""
curseur.execute(req,[pok[0], pok[1], pok[2], id_type1, id_type2, *pok[5:]] )
con.commit()
con.close()
curseur.execute(req,[pok[0], pok[1], pok[2], id_type1, id_type2, *pok[5:]] )
con.commit()
con.close()
        
