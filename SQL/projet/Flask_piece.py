from flask import Flask, render_template, request
import sqlite3
from random import sample

app = Flask(__name__)

connexion = sqlite3.connect("collection_21p.db")

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
        if 'nom' in request.form or 'nb_ex' in request.form or 'emet' in request.form or 'typ' in request.form or 'date' in request.form or 'dev' in request.form or 'comp' in request.form or 'pds' in request.form or 'diam' in request.form or 'ep' in request.form or 'forme' in request.form or 'demo' in request.form or 'idr' in request.form :
            nom_piece = request.form['nom']
            nb_ex_piece = request.form['nb_ex']
            emetteur_piece = request.form['emet']
            typ_piece = request.form['typ']            
            date_piece = request.form['date']
            devise_piece = request.form['dev']
            composition_piece = request.form['comp']
            poids_piece = request.form['pds']
            dimension_piece = request.form['dim']    
            epaisseur_piece = request.form['ep']
            forme_piece = request.form['forme']
            demonetisee_piece = request.form['demo']
            indice_rarete_piece = request.form['idr']             
            rep = f"""SELECT * FROM csv_piece WHERE nom LIKE '%{nom_piece}%' AND nb_ex LIKE '%{nb_ex_piece}%' AND emetteur LIKE '%{emetteur_piece}%' AND type LIKE '%{typ_piece}%' AND date LIKE '%{date_piece}%'
                        AND devise LIKE '%{devise_piece}%' AND composition LIKE '%{composition_piece}%' AND poids LIKE '%{poids_piece}%' AND dimension LIKE '%{dimension_piece}%' AND epaisseur LIKE '%{epaisseur_piece}%'
                        AND forme LIKE '%{forme_piece}%' AND demonetisee LIKE '%{demonetisee_piece}%' AND indice_de_rarete LIKE '%{indice_rarete_piece}%' ;"""
            result = curseur.execute(rep).fetchall()
            connexion.close()
            print(rep)
            if result == []:
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
    result = curseur.execute("SELECT idP, avers, revers FROM csv_piece;").fetchall()
    connexion.close()   
    return render_template('pieceotheque.html', repetition = result)


@app.route('/tri' ,methods = ['POST'])
def tri():  #fonction pour afficher toutes les pièces selon leurs nombres
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    if request.method == 'POST':
        if 'nb_ex' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY nb_ex ASC;").fetchall()
        elif 'tri_emet' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY emetteur ASC;").fetchall()
        elif 'tri_typ' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY type ASC;").fetchall()
        elif 'tri_date' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY date ASC;").fetchall()
        elif 'tri_dev' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY devise ASC;").fetchall()
        elif 'tri_comp' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY composition ASC;").fetchall()
        elif 'tri_pds' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY poids ASC;").fetchall()
        elif 'tri_dim' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY dimension ASC;").fetchall()
        elif 'tri_ep' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY epaisseur ASC;").fetchall()
        elif 'tri_forme' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY forme ASC;").fetchall()
        elif 'tri_demo' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY demonetisee ASC;").fetchall()
        elif 'tri_idr' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY indice_de_rarete ASC;").fetchall()
        elif 'tri_nb_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY nb_ex DESC;").fetchall()
        elif 'tri_emet_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY emetteur DESC;").fetchall()
        elif 'tri_typ_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY type DESC;").fetchall()
        elif 'tri_date_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY date DESC;").fetchall()
        elif 'tri_dev_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY devise DESC;").fetchall()
        elif 'tri_idr_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY indice_de_rarete DESC;").fetchall()
        elif 'tri_demo_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY demonetisee DESC;").fetchall()
        elif 'tri_forme_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY forme DESC;").fetchall()
        elif 'tri_ep_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY epaisseur DESC;").fetchall()
        elif 'tri_dim_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY dimension DESC;").fetchall()
        elif 'tri_pds_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY poids DESC;").fetchall()
        elif 'tri_comp_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY composition DESC;").fetchall()
        connexion.close()
        return render_template('tri.html', repetition = result)
    else:
        return render_template('vide.html')
        
        
@app.route('/pieceotheque_D',methods = ['GET'])
def pieceotheque_D():  #fonction pour afficher toutes les pièces de manière descendante
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    result = curseur.execute("SELECT idP, avers, revers FROM csv_piece;").fetchall()
    connexion.close()   
    return render_template('pieceotheque_D.html', repetition = result)


        

connexion.close()

if __name__ == "__main__":
    app.run()  
