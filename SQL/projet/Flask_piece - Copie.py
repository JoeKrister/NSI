from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

connexion = sqlite3.connect("collection.db")
curseur = connexion.cursor()
connexion.commit()

@app.route('/')
def recherche():
    return render_template("recherche.html")

    
@app.route('/resultats',methods = ['POST'])
def resultats():
    connexion = sqlite3.connect("collection.db")
    curseur = connexion.cursor()
    if request.method == 'POST':
        if 'nom' in request.form:
            nom_piece = request.form['nom']
            donnee = (str(nom_piece))
            rep = f"""SELECT date FROM collection_piece WHERE nom LIKE '%{donnee}%';"""
            result = curseur.execute(rep).fetchone()
            connexion.close()
            return render_template('resultats.html', repetition = result)
        
        else:
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
            donnee = [nb_ex_piece, date_piece, emetteur_piece, composition_piece, poid_piece, forme_piece, epaisseur_piece,
                      diametre_piece, demonetisee_piece, indice_rarete_piece, typ_piece, devise_piece]
            rep = f"""SELECT * FROM collection_piece WHERE nb_ex LIKE '%{nb_ex_piece}%' AND date LIKE '%{date_piece}%' AND emet LIKE '%{emetteur_piece}%' AND comp LIKE '%{composition_piece}%'
                        AND pd LIKE '%{poids_piece}%' AND forme LIKE '%{forme_piece}%' AND ed LIKE '%{epaisseur_piece}%' AND diam LIKE '%{diametre_piece}%' AND demo LIKE '%{demonetisee_piece}%'
                        AND idr LIKE '%{indice_rarete_piece}%' AND typ LIKE '%{typ_piece}%' AND dev LIKE '%{devise_piece}%';"""
            result = curseur.execute(rep).fetchall()
            connexion.close()
            return render_template('resultats.html', repetition = result)


@app.route('/pieceotheque/')
def tri():
    
    return render_template('pieceotheque.html')


connexion.close()

if __name__ == "__main__":
    app.run()  