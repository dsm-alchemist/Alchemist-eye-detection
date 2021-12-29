# Import Library
from flask import Flask, request
from parameter import default_path

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route("/upload", methods=["POST"])
def upload():
    uploaded_files = request.files.getlist("files")
    for img in uploaded_files:
        img.save(default_path + '/img/' + str(uploaded_files.index(img) + 1) + '.JPG')
    print(uploaded_files)
    return ""


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)