import sqlite3

#Connexion
connexion = sqlite3.connect('collection.db')

#Récupération d'un curseur
curseur = connexion.cursor()

#Validation
connexion.commit()

#Parcours des enregistrements....


# 
# donnee = ("1900", )
# rep = curseur.execute("SELECT nom FROM collection_piece WHERE date =?", donnee).fetchone()
# while rep:
#     print(rep)
#     rep = curseur.fetchone()

rep = curseur.execute("SELECT * FROM collection_piece" ).fetchone()
while rep:
    print(rep)
    rep = curseur.fetchone()

#Déconnexion
connexion.close()

# 
# curseur.execute("SELECT * FROM scores")
# resultats = curseur.fetchall()
# for resultat in resultats:
#     print(resultat)