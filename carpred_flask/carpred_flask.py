import numpy as np
from flask import Flask, request, render_template, jsonify
import pandas as pd
import pickle
 
app =Flask(__name__)
model = pickle.load(open('pipeline.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    data = request.form.to_dict()

    new_entry = pd.DataFrame(
        {'brand': [str(data['brand'])],
        'milage': [int(data['milage'])],
        'accident': [str(data['accident'])],
        'clean_title': [str(data['clean_title'])],
        'interior_color': [str(data['interior_color'])],
        'exterior_color': [str(data['exterior_color'])],
        'tsm': [str(data['tsm'])],
        'fuel': [str(data['fuel'])],
        'Engine_Displacement': [float(data['Engine_Displacement'])],
        'age': [int(data['age'])]}
    )

    prediction = model.predict(new_entry)
    output = round(prediction[0], 2)

   
    return render_template('index.html', prediction_text='Predicted Price: ${}'.format(output))
    

if __name__ == "__main__":
    app.run(debug=True)