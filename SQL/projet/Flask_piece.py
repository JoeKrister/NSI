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



### Fonctions de tri ascendant



@app.route('/pieceotheque',methods = ['GET'])
def pieceotheque():  #fonction pour afficher toutes les pièces
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    result = curseur.execute("SELECT idP, avers, revers FROM csv_piece;").fetchall()
    connexion.close()   
    return render_template('pieceotheque.html', repetition = result)


@app.route('/tri_nombre' ,methods = ['POST'])
def tri_nombre():  #fonction pour afficher toutes les pièces selon leurs nombres
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    if request.method == 'POST':
        if 'tri_nb' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY nb_ex ASC;").fetchall()
            connexion.close()
            return render_template('tri_nombre.html', repetition = result)
        else:
            return render_template('vide.html')        
    else:
        return render_template('vide.html')


@app.route('/tri_emetteur' ,methods = ['POST'])
def tri_emetteur():  #fonction pour afficher toutes les pièces selon leur emetteur
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    if request.method == 'POST':
        if 'tri_emet' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY emetteur ASC;").fetchall()
            connexion.close()
            return render_template('tri_emetteur.html', repetition = result)
        else:
            return render_template('vide.html')        
    else:
        return render_template('vide.html')
        

@app.route('/tri_type' ,methods = ['POST'])
def tri_type():  #fonction pour afficher toutes les pièces selon leur type
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    if request.method == 'POST':
        if 'tri_typ' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY type ASC;").fetchall()
            connexion.close()
            return render_template('tri_type.html', repetition = result)
        else:
            return render_template('vide.html')        
    else:
        return render_template('vide.html')
    
    
@app.route('/tri_date' ,methods = ['POST'])
def tri_date(): #fonction pour afficher toutes les pièces selon leur date
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    if request.method == 'POST':
        if 'tri_date' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY date ASC;").fetchall()
            connexion.close()
            return render_template('tri_date.html', repetition = result)
        else:
            return render_template('vide.html')        
    else:
        return render_template('vide.html')
        

@app.route('/tri_devise' ,methods = ['POST'])
def tri_devise(): #fonction pour afficher toutes les pièces selon leur devise
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    if request.method == 'POST':
        if 'tri_dev' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY devise ASC;").fetchall()
            connexion.close()
            return render_template('tri_devise.html', repetition = result)
        else:
            return render_template('vide.html')        
    else:
        return render_template('vide.html')


@app.route('/tri_composition' ,methods = ['POST'])
def tri_composition(): #fonction pour afficher toutes les pièces selon leur composition
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    if request.method == 'POST':
        if 'tri_comp' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY composition ASC;").fetchall()
            connexion.close()
            return render_template('tri_composition.html', repetition = result)
        else:
            return render_template('vide.html')        
    else:
        return render_template('vide.html')
        

@app.route('/tri_poids' ,methods = ['POST'])
def tri_poids(): #fonction pour afficher toutes les pièces selon leur poids
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    if request.method == 'POST':
        if 'tri_pds' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY poids ASC;").fetchall()
            connexion.close()
            return render_template('tri_poids.html', repetition = result)
        else:
            return render_template('vide.html')        
    else:
        return render_template('vide.html')
        

@app.route('/tri_dimension' ,methods = ['POST'])
def tri_dimension(): #fonction pour afficher toutes les pièces selon leur dimension
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    if request.method == 'POST':
        if 'tri_dim' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY dimension ASC;").fetchall()
            connexion.close()
            return render_template('tri_dimension.html', repetition = result)
        else:
            return render_template('vide.html')        
    else:
        return render_template('vide.html')
        
        
@app.route('/tri_epaisseur' ,methods = ['POST'])
def tri_epaisseur(): #fonction pour afficher toutes les pièces selon leur épaisseur
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    if request.method == 'POST':
        if 'tri_ep' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY epaisseur ASC;").fetchall()
            connexion.close()
            return render_template('tri_epaisseur.html', repetition = result)
        else:
            return render_template('vide.html')        
    else:
        return render_template('vide.html')
        
        
@app.route('/tri_forme' ,methods = ['POST'])
def tri_forme(): #fonction pour afficher toutes les pièces selon leur forme
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    if request.method == 'POST':
        if 'tri_forme' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY forme ASC;").fetchall()
            connexion.close()
            return render_template('tri_forme.html', repetition = result)
        else:
            return render_template('vide.html')        
    else:
        return render_template('vide.html')


@app.route('/tri_demonetise' ,methods = ['POST'])
def tri_demonetise(): #fonction pour afficher toutes les pièces selon leur demonetisation
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    if request.method == 'POST':
        if 'tri_demo' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY demonetisee ASC;").fetchall()
            connexion.close()
            return render_template('tri_demonetise.html', repetition = result)
        else:
            return render_template('vide.html')        
    else:
        return render_template('vide.html')
        
        
@app.route('/tri_idr' ,methods = ['POST'])
def tri_idr(): #fonction pour afficher toutes les pièces selon leur indice de rareté
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    if request.method == 'POST':
        if 'tri_idr' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY indice_de_rarete ASC;").fetchall()
            connexion.close()
            return render_template('tri_idr.html', repetition = result)
        else:
            return render_template('vide.html')        
    else:
        return render_template('vide.html')


### Fonctions de tri par descendant
        

@app.route('/pieceotheque_D',methods = ['GET'])
def pieceotheque_D():  #fonction pour afficher toutes les pièces de manière descendante
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    result = curseur.execute("SELECT idP, avers, revers FROM csv_piece;").fetchall()
    connexion.close()   
    return render_template('pieceotheque_D.html', repetition = result)


@app.route('/tri_nombre_D' ,methods = ['POST'])
def tri_nombre_D():  #fonction pour afficher toutes les pièces selon leurs nombres
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    if request.method == 'POST':
        if 'tri_nb_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY nb_ex DESC;").fetchall()
            connexion.close()
            return render_template('tri_nombre_D.html', repetition = result)
        else:
            return render_template('vide.html')        
    else:
        return render_template('vide.html')


@app.route('/tri_emetteur_D' ,methods = ['POST'])
def tri_emetteur_D():  #fonction pour afficher toutes les pièces selon leur emetteur
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    if request.method == 'POST':
        if 'tri_emet_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY emetteur DESC;").fetchall()
            connexion.close()
            return render_template('tri_emetteur_D.html', repetition = result)
        else:
            return render_template('vide.html')        
    else:
        return render_template('vide.html')
        

@app.route('/tri_type_D' ,methods = ['POST'])
def tri_type_D():  #fonction pour afficher toutes les pièces selon leur type
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    if request.method == 'POST':
        if 'tri_typ_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY type DESC;").fetchall()
            connexion.close()
            return render_template('tri_type_D.html', repetition = result)
        else:
            return render_template('vide.html')        
    else:
        return render_template('vide.html')
    
    
@app.route('/tri_date_D' ,methods = ['POST'])
def tri_date_D(): #fonction pour afficher toutes les pièces selon leur date
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    if request.method == 'POST':
        if 'tri_date_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY date DESC;").fetchall()
            connexion.close()
            return render_template('tri_date_D.html', repetition = result)
        else:
            return render_template('vide.html')        
    else:
        return render_template('vide.html')
        

@app.route('/tri_devise_D' ,methods = ['POST'])
def tri_devise_D(): #fonction pour afficher toutes les pièces selon leur devise
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    if request.method == 'POST':
        if 'tri_dev_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY devise DESC;").fetchall()
            connexion.close()
            return render_template('tri_devise_D.html', repetition = result)
        else:
            return render_template('vide.html')        
    else:
        return render_template('vide.html')


@app.route('/tri_composition_D' ,methods = ['POST'])
def tri_composition_D(): #fonction pour afficher toutes les pièces selon leur composition
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    if request.method == 'POST':
        if 'tri_comp_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY composition DESC;").fetchall()
            connexion.close()
            return render_template('tri_composition_D.html', repetition = result)
        else:
            return render_template('vide.html')        
    else:
        return render_template('vide.html')
        

@app.route('/tri_poids_D' ,methods = ['POST'])
def tri_poids_D(): #fonction pour afficher toutes les pièces selon leur poids
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    if request.method == 'POST':
        if 'tri_pds_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY poids DESC;").fetchall()
            connexion.close()
            return render_template('tri_poids_D.html', repetition = result)
        else:
            return render_template('vide.html')        
    else:
        return render_template('vide.html')
        

@app.route('/tri_dimension_D' ,methods = ['POST'])
def tri_dimension_D(): #fonction pour afficher toutes les pièces selon leur dimension
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    if request.method == 'POST':
        if 'tri_dim_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY dimension DESC;").fetchall()
            connexion.close()
            return render_template('tri_dimension_D.html', repetition = result)
        else:
            return render_template('vide.html')        
    else:
        return render_template('vide.html')
        
        
@app.route('/tri_epaisseur_D' ,methods = ['POST'])
def tri_epaisseur_D(): #fonction pour afficher toutes les pièces selon leur épaisseur
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    if request.method == 'POST':
        if 'tri_ep_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY epaisseur DESC;").fetchall()
            connexion.close()
            return render_template('tri_epaisseur_D.html', repetition = result)
        else:
            return render_template('vide.html')        
    else:
        return render_template('vide.html')
        
        
@app.route('/tri_forme_D' ,methods = ['POST'])
def tri_forme_D(): #fonction pour afficher toutes les pièces selon leur forme
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    if request.method == 'POST':
        if 'tri_forme_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY forme DESC;").fetchall()
            connexion.close()
            return render_template('tri_forme_D.html', repetition = result)
        else:
            return render_template('vide.html')        
    else:
        return render_template('vide.html')


@app.route('/tri_demonetise_D' ,methods = ['POST'])
def tri_demonetise_D(): #fonction pour afficher toutes les pièces selon leur demonetisation
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    if request.method == 'POST':
        if 'tri_demo_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY demonetisee DESC;").fetchall()
            connexion.close()
            return render_template('tri_demonetise_D.html', repetition = result)
        else:
            return render_template('vide.html')        
    else:
        return render_template('vide.html')
        
        
@app.route('/tri_idr_D' ,methods = ['POST'])
def tri_idr_D(): #fonction pour afficher toutes les pièces selon leur indice de rareté
    connexion = sqlite3.connect("collection_21p.db")
    curseur = connexion.cursor()
    if request.method == 'POST':
        if 'tri_idr_D' in request.form:
            result = curseur.execute("SELECT * FROM csv_piece ORDER BY indice_de_rarete DESC;").fetchall()
            connexion.close()
            return render_template('tri_idr_D.html', repetition = result)
        else:
            return render_template('vide.html')        
    else:
        return render_template('vide.html')



connexion.close()

if __name__ == "__main__":
    app.run()  
