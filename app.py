from flask import Flask, render_template, request, send_from_directory,abort,send_file
from datetime import datetime
#from pymongo import MongoClient
import os
from werkzeug.utils import secure_filename
from utils import *
from flask import session

current_path = os.getcwd()+'/static/files'
file_list = os.listdir(current_path)

app = Flask(__name__, static_url_path="/", static_folder="static/", template_folder="templates/")

print(current_path)
@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST' or 'GET':

        if not os.path.exists(current_path):
            return abort(404)

        # Check if path is a file and serve
        if os.path.isfile(current_path):
            return send_file(current_path)

            # Show directory contents
        files = os.listdir(current_path)
        files_list = ['files/'+file for file in files]

        return render_template('index.html',files=files_list,current_path=current_path)


@app.route('/fileupload', methods=['POST', 'GET'])
def fileupload():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(current_path, '/'+filename))

        return '제출 성공'



if __name__ == "__main__":
    app.run(debug=True)