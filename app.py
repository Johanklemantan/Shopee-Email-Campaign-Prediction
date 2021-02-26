from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# halaman home
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/visualize', methods=['POST', 'GET'])
def visualize():
    return render_template('visualize.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    return render_template('predict.html')

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
            return render_template('resultno.html', data=input, pred=results,hasil = prediksi)
            
        else:
            results = 'Read the Promotion Email'
            return render_template('resultyes.html', data=input, pred=results, hasil = prediksi)

        
if __name__ == '__main__':
    
    filename = 'best_model_shopee_email'

    model = joblib.load(filename)

    app.run(debug=True)