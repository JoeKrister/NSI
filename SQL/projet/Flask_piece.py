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
        nom_piece = request.form['nom']
        
        donnee = (str(nom_piece))
        rep = f"""SELECT * FROM collection_piece WHERE nom LIKE '%{donnee}%';"""
        result = curseur.execute(rep).fetchone()
        connexion.close()
        return render_template('resultats.html', repetition = result)


@app.route('/pieceotheque/')
def tri():
    
    return render_template('pieceotheque.html')


connexion.close()

if __name__ == "__main__":
    app.run()  