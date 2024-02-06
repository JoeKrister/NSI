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
            ### si une requete est faite, faire recherche dans la base de donnée
            nom = request.form['nom']
            nb_ex = request.form['nb_ex']
            emet = request.form['emet']
            typ = request.form['typ']            
            date = request.form['date']
            dev = request.form['dev']
            comp = request.form['comp']
            pds = request.form['pds']
            dim = request.form['dim']    
            ep = request.form['ep']
            forme = request.form['forme']
            demo = request.form['demo']
            idr = request.form['idr']
            rep = f"""SELECT * FROM csv_piece WHERE nom LIKE '%{nom}%' AND nb_ex LIKE '%{nb_ex}%' AND emetteur LIKE '%{emet}%' AND type LIKE '%{typ}%' AND date LIKE '%{date}%'
                        AND devise LIKE '%{dev}%' AND composition LIKE '%{comp}%' AND poids LIKE '%{pds}%' AND dimension LIKE '%{dim}%' AND epaisseur LIKE '%{ep}%'
                        AND forme LIKE '%{forme}%' AND demonetisee LIKE '%{demo}%' AND indice_de_rarete LIKE '%{idr}%' ;"""
            result = curseur.execute(rep).fetchall()
            connexion.close()
            if result == []:### si que des requetes vides, afficher page vide
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
            ### Déscendant
        elif 'nb_ex_D' in request.form:
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
