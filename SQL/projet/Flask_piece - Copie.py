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
            result = curseur.execute(rep).fetchone()[0]
            connexion.close()
            return render_template('resultats.html', repetition = result)
        
        else:
            nb_ex_piece = request.form['nb_ex']
            date_piece = request.form['date']
            emetteur_piece = request.form['emet']
            composition_piece = request.form['comp']
            poid_piece = request.form['pd']
            forme_piece = request.form['forme']
            epaisseur_piece = request.form['ep']
            diametre_piece = request.form['diam']
            demonetisee_piece = request.form['demo']
            indice_rarete_piece = request.form['idr']
            typ_piece = request.form['typ']
            devise_piece = request.form['dev']
            connexion.close()
            return render_template('resultats.html', nb_ex = nb_ex_piece, date = date_piece, emet = emetteur_piece,
                               comp = composition_piece, pd = poid_piece, forme = forme_piece, ep = epaisseur_piece,
                               diam = diametre_piece , demo =demonetisee_piece,  idr = indice_rarete_piece,
                               typ = typ_piece, dev = devise_piece)


@app.route('/pieceotheque/')
def tri():
    
    return render_template('pieceotheque.html')


connexion.close()

if __name__ == "__main__":
    app.run()  