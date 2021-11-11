# Import Library
import os
from flask import Flask, flash, request, redirect
from flask import url_for, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'random string'    # 프레임워크 상에서 꼭 넣으라고 요구함.

@app.route('/')


if __name__ == '__main__':
    app.run()