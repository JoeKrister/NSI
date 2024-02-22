from flask import Flask, render_template, request
import sqlite3
from random import sample

app = Flask(__name__)

connexion = sqlite3.connect("collection_21p.db")

@app.route('/')
def accueil(): #affiche simplemennt la page d'accueil
    return render_template('accueil.html')
    

@app.route('/recherche')
def recherche(): #fonction pour afficher la 1ere page/ page principale
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    rep = """SELECT  idP, avers, revers FROM csv_piece;""" #la variable rep est initialisée avec les données de la db (l'ip de la pièce, l'image avant et arrière) 
    all_results = curseur.execute(rep).fetchall() #recupère toutes les données 
    result = sample(all_results, min(5, len(all_results))) #sélectionne 5 résultats aléatoires
    connexion.close()
    return render_template('recherche.html', repetition = result) #variable repetition pour la boucle dans recherche.html



@app.route('/resultats',methods = ['POST'])
def resultats():
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    if request.method == 'POST':       
        if 'nom' in request.form or 'nb_ex' in request.form or 'emet' in request.form or 'typ' in request.form or 'date' in request.form or 'dev' in request.form or 'comp' in request.form or 'pds' in request.form or 'diam' in request.form or 'ep' in request.form or 'forme' in request.form or 'demo' in request.form or 'idr' in request.form :
            # si une requete est faite, faire recherche dans la base de donnée
            rep = f"""SELECT * FROM csv_piece WHERE nb_ex = {request.form['nb_ex']}"""
            if request.form['nom'] != "" :
                rep += f" AND nom LIKE '%{request.form['nom']}%'"
            if request.form['emet'] != "" :
                rep += f" AND emetteur LIKE '%{request.form['emet']}%'"
            if request.form['typ'] != "":
                rep += f" AND type_p LIKE '%{request.form['typ']}%'"
            if request.form['date'] != "0" :
                rep += f" AND date ='{request.form['date']}'"
            if request.form['dev'] != "":
                rep += f" AND devise LIKE '%{request.form['dev']}%'"
            if request.form['comp'] != "":
                rep += f" AND composition LIKE '%{request.form['comp']}%'"
            if request.form['pds'] != "0":
                rep += f" AND poids LIKE '%{request.form['pds']}%'"
            if request.form['dim'] != "0":
                rep += f" AND dimension LIKE '%{request.form['dim']}%'"
            if request.form['ep'] != "0":
                rep += f" AND epaisseur LIKE '%{request.form['ep']}%'"
            if request.form['forme'] != "":
                rep += f" AND forme LIKE '%{request.form['forme']}%'"
            if request.form['demo'] != "":
                rep += f" AND demonetisee LIKE '%{request.form['demo']}%'"
            if request.form['idr'] != "0":
                rep += f" AND indice_de_rarete LIKE '%{request.form['idr']}%'"
            result = curseur.execute(rep).fetchall()
            connexion.close()
            if result == []:# si il n'y a que des requetes vides, afficher page vide
                return render_template('vide.html')
            else:
                return render_template('resultats.html', repetition = result)
        else:
            return render_template('vide.html')
    else:
        return render_template('vide.html')
            

@app.route('/piece/<int:idP>')
def piece(idP):  #fonction pour l'affichage unique de la pièce
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    result = curseur.execute("SELECT * FROM csv_piece WHERE idP=?;", (idP,)).fetchall() #selectionne la ligne selon l'ip rentrée
    connexion.close()
    return render_template('piece.html', repetition = result)



### Fonctions de tri


@app.route('/pieceotheque',methods = ['GET'])
def pieceotheque():  #fonction pour afficher toutes les pièces
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    result = curseur.execute("SELECT idP, avers, revers FROM csv_piece;").fetchall() #selectionne l'ip, l'image de l'avers et de l'envers
    connexion.close()
    return render_template('pieceotheque.html', repetition = result)


@app.route('/tri' ,methods = ['POST'])
def tri():  #fonction pour afficher toutes les pièces selon leurs nombres
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    if request.method == 'POST':
        ### Ascendant
        if 'nb_ex' in request.form: #si il y a un request.form de fait, ça tri dans la base de donnée selon le request.form utilisé
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY nb_ex ASC;").fetchall()
            tri = "Tri par nombre d'exemplaire croissant." 
            cle = ("Nombre(s) d'exemplaire(s)",2) #le numéro correspond à la colonne dans la base de donnée
        elif 'tri_emet' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY emetteur ASC;").fetchall()
            tri = "Tri par émetteur croissant."
            cle = ("Émetteur",3)
        elif 'tri_type_p' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY type_p ASC;").fetchall()
            tri = "Tri par type croissant."
            cle = ("Type",4)
        elif 'tri_date' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY date ASC;").fetchall()
            tri = "Tri par année croissante"
            cle = ("Année", 5)
        elif 'tri_dev' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY devise ASC;").fetchall()
            tri = "Tri par devise croissante"
            cle = ("Devise", 6)
        elif 'tri_comp' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY composition ASC;").fetchall()
            tri = "Tri par composition croissante"
            cle = ("Composition", 7)
        elif 'tri_pds' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY poids ASC;").fetchall()
            tri = "Tri par poids croissante"
            cle = ("Poids(g)", 8)
        elif 'tri_dim' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY dimension ASC;").fetchall()
            tri = "Tri par dimension croissante"
            cle = ("Dimension(mm)", 9)
        elif 'tri_ep' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY epaisseur ASC;").fetchall()
            tri = "Tri par épaisseur croissante"
            cle = ("Épaisseur(mm)", 10)
        elif 'tri_forme' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY forme ASC;").fetchall()
            tri = "Tri par forme croissante"
            cle = ("Forme", 11)
        elif 'tri_demo' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY demonetisee ASC;").fetchall()
            tri = "Tri par démonétisation croissante"
            cle = ("Démonétisée", 12)
        elif 'tri_idr' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY indice_de_rarete ASC;").fetchall()
            tri = "Tri par indice de rareté croissante"
            cle = ("Indice de rareté", 13)
            ### Déscendant
        elif 'nb_ex_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY nb_ex DESC;").fetchall()
            tri = "Tri par nombre d'exemplaire décroissant."
            cle = ("Nombre(s) d'exemplaire(s)",2)
        elif 'tri_emet_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY emetteur DESC;").fetchall()
            tri = "Tri par émetteur décroissant."
            cle = ("Émetteur",3)
        elif 'tri_type_p_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY type_p DESC;").fetchall()
            tri = "Tri par type décroissant."
            cle = ("Type",4)
        elif 'tri_date_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY date DESC;").fetchall()
            tri = "Tri par année décroissante."
            cle = ("Année",5)
        elif 'tri_dev_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY devise DESC;").fetchall()
            tri = "Tri par devise décroissante."
            cle = ("Devise",6)
        elif 'tri_comp_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY composition DESC;").fetchall()
            tri = "Tri par composition décroissante."
            cle = ("Composition",7)
        elif 'tri_pds_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY poids DESC;").fetchall()
            tri = "Tri par poids décroissant."
            cle = ("Poids(g)",8)
        elif 'tri_dim_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY dimension DESC;").fetchall()
            tri = "Tri par dimension décroissante."
            cle = ("Dimension(mm)",9)
        elif 'tri_ep_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY epaisseur DESC;").fetchall()
            tri = "Tri par épaisseur décroissante."
            cle = ("Épaisseur(mm)",10)
        elif 'tri_forme_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY forme DESC;").fetchall()
            tri = "Tri par forme décroissante."
            cle = ("Forme",11)
        elif 'tri_demo_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY demonetisee DESC;").fetchall()
            tri = "Tri par démonétisation décroissante."
            cle = ("Démonétisation",12)
        elif 'tri_idr_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY indice_de_rarete DESC;").fetchall()
            tri = "Tri par indice de rareté décroissant."
            cle = ("Indice de rareté",13)
        connexion.close()
        return render_template('tri.html', repetition = result, tri = tri, cle=cle)
    else:
        return render_template('vide.html')



# /!\ en test, pas fini !!
@app.route('/enregistrement',methods = ['GET'])
def enregistrement():  #fonction pour pouvoir enregistrer des pièces
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    if 'nb_ex' in request.form:
        nb_ex = request.form['nb_ex']
        curseur.execute(f"""INSERT INTO csv_piece(nb_ex) VALUES({nb_ex});""")
    connexion.close()   
    return render_template('enregistrement.html')
        

connexion.close()

if __name__ == "__main__":
    app.run()  
