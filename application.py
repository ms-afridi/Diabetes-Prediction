from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

application = Flask(__name__)
app = application

scaler = pickle.load(open("Model/scalerr.pkl", "rb"))
model = pickle.load(open("Model/log_reg.pkl", "rb"))


## Route for home page

@app.route('/')
def index():
    return render_template('index.html')

## Route for single data point prediction
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    result = ""

    if request.method == 'POST':

        Pregancies = int(request.form.get("Pregnancies"))
        Glucose = float(request.form.get('Glucose'))
        BloodPressure = float(request.form.get('BloodPressure'))
        SkinThikness = float(request.form.get('SkinThikness'))
        Insulin = float(request.form.get('Insuline'))
        BMI = float(request.form.get('BMI'))
        DiabetesPedigreefunction = float(request.form.get('DiabetesPedigreeFunction'))
        Age = float(request.form.get('Age'))

        new_data = scaler.transform([[Pregancies, Glucose, BloodPressure, SkinThikness, Insulin, BMI, DiabetesPedigreefunction, Age]])
        predict = model.predict(new_data)

        if predict[0] == 1:
            result = 'Diabetic'
        else:
            result = 'NON Diabetic'

        return render_template('single_prediction.html', result = result)

    else:
        return render_template('home.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0")
