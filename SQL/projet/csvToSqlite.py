import csv, sqlite3

con = sqlite3.connect('collection_piece.db')

with open('collectio_piece.csv', newline='', encoding='utf8') as csvfile:
    reader = csv.reader(csvfile)
    curseur=con.cursor()
    curseur.execute("""DROP TABLE IF EXISTS piece""")
    curseur.execute("""
    CREATE TABLE IF NOT EXISTS collection_piece (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    nom TEXT,
    nb_exemple SMALLINT,
    emetteur VARCHAR(90),
    type VARCHAR(90),
    date SMALLINT,
    devise VARCHAR(90),
    composition VARCHAR(20),
    poids REAL,
    diametre REAL,
    epaisseur REAL,
    forme VARCHAR(20),
    demonetisee BOOLEAN,
    indice_rarete SMALLINT,
    avers TEXT,
    envers TEXT)
    """)
    for line in list(reader)[1:] :
        req = f"""
    INSERT INTO collection_piece (id, nom, nb_exemple, emetteur, type, date,
    devise, composition,poids, diametre, epaisseur, forme, demonetisee, indice_rarete, avers, envers
    ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);
        """
        curseur.execute(req,[*line] )
con.commit()
con.close()
        
