# Import Library
from flask import Flask, request, jsonify
from flask_cors import CORS
from ai_response import ai_response

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "Hello\nThis is on Alchemist Timer"

@app.route("/ai", methods=["POST"])
def upload():
    uploaded_files = request.files.getlist("files")
    return jsonify(ai_response(*uploaded_files))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)