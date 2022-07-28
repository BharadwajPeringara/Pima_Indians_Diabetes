# importing revelant libraries 

from flask import Flask, request, url_for, redirect, render_template
import joblib
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

model = joblib.load('model.pkl')
scale = joblib.load('scale.pkl')

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    pregnancies = request.form['1']
    glucose = request.form['2']
    bloodPressure = request.form['3']
    skinThickness = request.form['4']
    insulin = request.form['5']
    bmi = request.form['6']
    dpf = request.form['7']
    age = request.form['8']

    # model predicting
    rowDf = pd.DataFrame([pd.Series([pregnancies, glucose, bloodPressure, skinThickness, insulin, bmi, dpf, age])])
    new_rowDf = pd.DataFrame(scale.transform(rowDf))
    print(f'{new_rowDf}')

    prediction = model.predict_proba(new_rowDf)
    print(f'Prediction values are {prediction[0][1]}')
    print(f'Prediction {round(prediction[0][1],4)*100}')
    print(f'Percent{round(prediction[0][0],4)*100}')
    if prediction[0][1] > 0.5:
        percentage = round(prediction[0][1], 4)*100
        return render_template('result.html', pred=f'You have chance of having diabetes.\n Probability of being a diabetic is {percentage}%')
    else:
        percentage = round(prediction[0][0], 4)*100
        return render_template('result.html', pred=f'Congratulations!!, You are in safe.\n Probability of being diabetic is {percentage}%')
    

if __name__ == '__main__':
    app.run(debug=True)

