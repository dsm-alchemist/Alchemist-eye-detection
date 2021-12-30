# Import Library
from flask import Flask, request, jsonify
from ai_response import ai_response

app = Flask(__name__)

@app.route("/", methods=["POST"])
def upload():
    uploaded_files = request.files.getlist("files")
    return jsonify(ai_response(*uploaded_files))