import pandas as pd
import numpy as np
import pickle
from flask import Flask, request, render_template
from sklearn.preprocessing import StandardScaler
sclr = StandardScaler()

# load pickle model

model = pickle.load(open('model.pkl','rb'))
sclr = pickle.load(open('scaler.pkl','rb'))

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    Open = request.form['Open']
    High = request.form['High']
    Low = request.form['Low']
    Adj_close = request.form['Adj_close']
    Volume = request.form['Volume']
    Year = request.form['Year']
    Month = request.form['Month']
    Day = request.form['Day']

    features = np.array([[Open,High,Low,Adj_close,Volume,Year,Month,Day]])
    features = sclr.transform(features)
    prediction = model.predict(features).reshape(1,-1)
    
    return render_template('index.html',output = prediction[0])

#main py

if __name__ == '__main__':
    app.run(debug=True)