import pandas as pd
import numpy as np
import pickle
from flask import Flask, request, render_template

# load pickle model

model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', method=['POST'])
def predict():
    pass

#main py

if __name__ == '__main__':
    app.run(debug=True)