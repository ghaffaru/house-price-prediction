from flask import Flask, render_template, request, url_for, flash, redirect, jsonify
from form import PredictionForm
import pandas as pd
import numpy as np
import joblib
import json

app = Flask(__name__)

app.config['SECRET_KEY'] = '15d1a4704a23a032d3695927a8e3dff5'


@app.route('/', methods=['GET', 'POST'])
def home():
    form = PredictionForm()
    if form.validate_on_submit():
        data = [form.bedrooms.data, form.bathrooms.data, form.sqft_living.data, form.sqft_lot.data,
                form.floors.data, form.sqft_above.data, form.sqft_lot15.data, form.yr_built.data,
                form.condition.data, form.zipcode.data]
        model = joblib.load('model.joblib')
        result = model.predict([data])
        actual_result = str(result).strip('[]')
        flash('Predicted Price: $' + actual_result, 'success')
        return redirect(url_for('home'))
    return render_template('index.html', form=form)


@app.route('/api/predict', methods=['POST'])
def predict():
    bedrooms = request.json['bedrooms']
    bathrooms = request.json['bathrooms']
    sqft_living = request.json['sqft_living']
    sqft_lot = request.json['sqft_lot']
    floors = request.json['floors']
    sqft_above = request.json['sqft_above']
    sqft_lot15 = request.json['sqft_lot15']
    yr_built = request.json['yr_built']
    condition = request.json['condition']
    zipcode = request.json['zipcode']

    data = [bedrooms,bathrooms,sqft_living,sqft_lot,floors,sqft_above,sqft_lot15,yr_built,
            condition,zipcode]

    model = joblib.load('model.joblib')
    result = model.predict([data])
    actual_result = str(result).strip('[]')

    return jsonify({'predicted': actual_result})


@app.route('/pred', methods=['POST'])
def dummy():

    return jsonify({'test': request.json})

if __name__ == "__main__":
    app.run(debug=True, port=36174)
