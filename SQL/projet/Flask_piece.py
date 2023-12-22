from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def recherche():
    return render_template("recherche.html")

    
@app.route('/resultats',methods = ['POST'])
def resultats():
    if request.method == 'POST':
        nom_piece = request.form['nom']
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

    return render_template('resultats.html', nom=nom_piece, nb_ex = nb_ex_piece, date = date_piece, emet = emetteur_piece,
                           comp = composition_piece, pd = poid_piece, forme = forme_piece, ep = epaisseur_piece,
                           diam = diametre_piece , demo =demonetisee_piece,  idr = indice_rarete_piece,
                           typ = typ_piece, dev = devise_piece)



@app.route('/pieceotheque/')
def tri():
    return render_template('pieceotheque.html')

if __name__ == "__main__":
    app.run()  