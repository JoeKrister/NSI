from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def recherche():
    return render_template('recherche.html')

@app.route('/resultats/')
def resultats():
    return render_template('resultats.html')

@app.route('/pieceotheque/')
def tri():
    return render_template('pieceotheque.html')

if __name__ == "__main__":
    app.run()  