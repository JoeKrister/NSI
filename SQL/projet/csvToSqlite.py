import csv, sqlite3

con = sqlite3.connect('pokemon.db')
liste_types = set()
pokemons=[]
with open('pokemon.csv', newline='', encoding='utf8') as csvfile:
    reader = csv.reader(csvfile)
    curseur=con.cursor()
    curseur.execute("""DROP TABLE IF EXISTS Pokemon""")
    curseur.execute("""DROP TABLE IF EXISTS Type""")
    curseur.execute("""
    CREATE TABLE IF NOT EXISTS Type (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,nom_type VARCHAR(30))
    """)
    
    curseur.execute("""
    CREATE TABLE IF NOT EXISTS Pokemon (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT,
    imageName TEXT,
    form VARCHAR(40),
    type1 INT,
    type2 INT,
    total INTEGER,
    hp INTEGER,
    attack INTEGER,
    defense INTEGER,
    sp_attack INTEGER,
    sp_defense INTEGER,
    speed INTEGER,
    generation INTEGER,
    FOREIGN KEY (type1) REFERENCES Type(id),
    FOREIGN KEY (type2) REFERENCES Type(id)
    )
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
        
        pokemons.append([name.lower(),imgname.lower(), line[2], type1, type2, *line[5:]])
con.commit()
con.close()
con = sqlite3.connect('pokemon.db')
curseur=con.cursor()
for typ in liste_types :
    req = f"""INSERT INTO Type(nom_type) VALUES (?);"""
    curseur.execute(req, [typ])
con.commit()
con.close()
con = sqlite3.connect('pokemon.db')
curseur=con.cursor()



for pok in pokemons :
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
        
    
    req = f"""
    INSERT INTO Pokemon (name, imagename, form, type1, type2, total, hp,
    attack, defense,sp_attack, sp_defense, speed, generation
    ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);
        """
    curseur.execute(req,[pok[0], pok[1], pok[2], id_type1, id_type2, *pok[5:]] )
con.commit()
con.close()
        
