from flask import Flask, jsonify
from flask_cors import CORS
import acteursfile
import videofile

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})  # This will enable CORS for all routes

@app.route('/')
def alleacteurs():
    return jsonify(acteursfile.geefAlleActeurs())

@app.route('/zoekopkenmerknaam/<naamdeel>')
def acteuropnaam(naamdeel):
    return jsonify(acteursfile.geefActeursOpNaam(naamdeel))

@app.route('/zoekopallekenmerken/<naamdeel>/<d>/<k>/<r>/<g>')
def acteuropallekenmerken(naamdeel,d,k,r,g):
    return jsonify(acteursfile.geefActeursOpAlleKenmerken(naamdeel,d,k,r,g))

@app.route('/zoeknullopcategorie/<c>')
def zoeknullopcategorie(c):
    return jsonify(acteursfile.zoeknullopcategorie(c))

@app.route('/kentoe/<c>/<w>/<i>')
def kentoe(c,w,i):
    return jsonify(acteursfile.kentoe(c,w,i))

@app.route('/volgendvideomomentopvragen/')
def volgendvideomomentopvragen():
    return jsonify(videofile.volgendvideomomentopvragen())

@app.route('/videomomentopslaan/<v>/<a>/<t>')
def videomomentopslaan(v,a,t):
    return jsonify(videofile.videomomentopslaan(v,a,t))

if __name__ == '__main__':
    app.run(debug=True)