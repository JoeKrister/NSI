from flask import Flask, render_template, request
import sqlite3
from random import randint, choice, sample

app = Flask(__name__)

connexion = sqlite3.connect("collection_21p.db")
curseur = connexion.cursor()
connexion.commit()

@app.route('/')
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
        if 'nom' in request.form or 'nb_ex' in request.form or 'date' in request.form or 'emet' in request.form or 'comp' in request.form or 'pd' in request.form or 'forme' in request.form or 'ep' in request.form or 'diam' in request.form or 'demo' in request.form or 'idr' in request.form or 'typ' in request.form or 'dev' in request.form :
            nom_piece = request.form['nom']
            nb_ex_piece = request.form['nb_ex']
            date_piece = request.form['date']
            emetteur_piece = request.form['emet']
            composition_piece = request.form['comp']
            poids_piece = request.form['pd']
            forme_piece = request.form['forme']
            epaisseur_piece = request.form['ep']
            diametre_piece = request.form['diam']
            demonetisee_piece = request.form['demo']
            indice_rarete_piece = request.form['idr']
            typ_piece = request.form['typ']
            devise_piece = request.form['dev']
            donnee = [nom_piece, nb_ex_piece, date_piece, emetteur_piece, composition_piece, poids_piece, forme_piece, epaisseur_piece,
                      diametre_piece, demonetisee_piece, indice_rarete_piece, typ_piece, devise_piece]
            rep = f"""SELECT * FROM csv_piece WHERE nom LIKE '%{nom_piece}%' AND nb_ex LIKE '%{nb_ex_piece}%' AND date LIKE '%{date_piece}%' AND emetteur LIKE '%{emetteur_piece}%' AND composition LIKE '%{composition_piece}%'
                        AND poids LIKE '%{poids_piece}%' AND forme LIKE '%{forme_piece}%' AND epaisseur LIKE '%{epaisseur_piece}%' AND dimension LIKE '%{diametre_piece}%' AND demonetisee LIKE '%{demonetisee_piece}%'
                        AND indice_de_rarete LIKE '%{indice_rarete_piece}%' AND type LIKE '%{typ_piece}%' AND devise LIKE '%{devise_piece}%';"""
            result = curseur.execute(rep).fetchall()
            connexion.close()
            if result == []:
                return render_template('vide.html')
            else:
                return render_template('resultats.html', repetition = result)

    
    


@app.route('/pieceotheque',methods = ['POST'])

def pieceotheque():  #pour tri: faire requetes sql pour chaque tri
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    if request.method == 'POST':
        rep = f"""SELECT * FROM csv_piece;"""
        result = curseur.execute(rep).fetchall()
        connexion.close()
        return render_template('pieceotheque.html', repetition = result)



@app.route('/piece/<int:idP>')

def piece(idP):
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    rep = "SELECT * FROM csv_piece WHERE idP=?;"
    result = curseur.execute(rep, (idP,)).fetchall()
    connexion.close()
    return render_template('piece.html', repetition = result)

    
    


connexion.close()

if __name__ == "__main__":
    app.run()  
