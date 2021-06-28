from flask import Flask, render_template, request, send_from_directory,abort,send_file
from datetime import datetime
#from pymongo import MongoClient
import os
from werkzeug.utils import secure_filename
from flask import session
from database import banji_conn,conn
from datetime import date


app = Flask(__name__, static_url_path="/", static_folder="static/", template_folder="templates/")
#app = Flask(__name__, template_folder="templates/")
whatdate = date.today()

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST' or 'GET':

        return render_template('index.html')


@app.route('/add',methods=['POST'])
def add_data():
    if request.method == 'POST' or 'GET':

        selected_size = request.form.getlist('options')
        selected_color = request.form.getlist('colors')
        recommended_names = str(request.form['recname'])


        sql_sentence = f"""
        insert into Labeling_image(image_path,animal_size,animal_color,recommand_name,collect_date) 
        values('pathtest', '{str(selected_size[0])}','{str(selected_color[0])}','{str(recommended_names)}', '{whatdate}');
        """

        curs = conn.cursor()
        curs.execute(sql_sentence)
        conn.commit()

        return render_template(
            'index.html',
            options=selected_size,
            colors = selected_color,
            recname=recommended_names)


if __name__ == "__main__":
    app.run(debug=True)