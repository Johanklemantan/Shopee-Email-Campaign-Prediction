from flask import Flask, render_template, request, redirect
import joblib
import pandas as pd
from flask_mysqldb import MySQL
import mysql.connector as sql

app = Flask(__name__)
model = joblib.load('best_model_shopee_email')
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Funicula8'
app.config['MYSQL_DB']='johan'
app.config['MYSQL_CURSORCLASS']='DictCursor'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('tryhome.html')

@app.route('/visualize', methods=['POST', 'GET'])
def visualize():
    return render_template('tryvisualize.html')

@app.route('/database')
def database():
    connection = sql.connect(
        host = "localhost",
        port = "3306",
        user = "root",
        password = "Funicula8",
        database = "johan"
        )
    c = connection.cursor(buffered=True)
    query = 'select * from sqldata LIMIT 1000;'
    c.execute(query)
    hasil_data = c.fetchall()
    return render_template('database.html', hasil_data=hasil_data)


@app.route('/predict', methods=['POST', 'GET'])
def predict():

    return render_template('trypredict.html')

@app.route('/background', methods=['POST', 'GET'])
def background():
    return render_template('background.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method=='POST':
        input = request.form

        df_to_predict = pd.DataFrame({
            'age': [input['age']],
            'domain': [input['domain']],
            'country': [input['country']],
            'day': [input['day']],
            'character_length': [input['character_length']],
            'last_time_open_email': [input['last_time_open_email']],
            'last_time_open_shopee': [input['last_time_open_shopee']],
            'last_time_checkout_shopee': [input['last_time_checkout_shopee']],
            'open_frequency': [input['open_frequency']],
            'login_frequency': [input['login_frequency']],
            'checkout_frequency': [input['checkout_frequency']]
        })

        prediksi = model.predict_proba(df_to_predict)[:,1]

        if prediksi < 0.49:
            results = 'Not Read the Promotion Email'
            return render_template('tryresultno.html', data=input, pred=results,hasil = prediksi)
            
        else:
            results = 'Read the Promotion Email'
            return render_template('tryresultyes.html', data=input, pred=results, hasil = prediksi)     
if __name__ == '__main__':
    app.run(debug=True)