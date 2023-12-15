import sqlite3

#Connexion
connexion = sqlite3.connect("basededonnees.db") 

#Récupération d'un curseur
curseur = connexion.cursor()

#Activation clés étrangères
curseur.execute("PRAGMA foreign_keys = ON") 

#Création table joueur puis score si elles n'existent pas encore
#Puis suppression des données dans joueurs (et dans scores aussi par cascade)
#afin d'éviter les répétitions d'enregistrements avec des exécutions multiples
curseur.executescript("""

    CREATE TABLE IF NOT EXISTS joueurs(
    id_joueur INTEGER PRIMARY KEY,
    pseudo TEXT,
    mdp TEXT);

    CREATE TABLE IF NOT EXISTS scores(
    id_score INTEGER PRIMARY KEY,
    fk_joueur INTEGER NOT NULL,
    valeur INTEGER,
    FOREIGN KEY(fk_joueur) REFERENCES joueurs(id_joueur)
    ON DELETE CASCADE);

    DELETE FROM joueurs;
""")

#Préparation des données
donnees_joueur = [
    ("toto", "123"),
    ("tata", "azerty"),
    ("titi", "qwerty")
]
donnees_score = [
    (1, 1000),
    (2, 750),
    (3, 500)
]

#Insertion des données dans table joueur puis score
curseur.executemany("INSERT INTO joueurs (pseudo, mdp) VALUES (?, ?)", donnees_joueur)
curseur.executemany("INSERT INTO scores (fk_joueur, valeur) VALUES (?, ?)", donnees_score)

#Validation des ajouts
connexion.commit()

#Affichage des données
for joueur in curseur.execute("SELECT * FROM joueurs"):
    print("joueur :", joueur)

for score in curseur.execute("SELECT * FROM scores"):
    print("score :", score)

#Déconnexion
connexion.close()