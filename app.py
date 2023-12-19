from flask import Flask, jsonify
from flask_cors import CORS
import acteursfile

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})  # This will enable CORS for all routes

@app.route('/')
def hello_world():
    return jsonify(acteursfile.geefAlleActeurs())

if __name__ == '__main__':
    app.run(debug=True)