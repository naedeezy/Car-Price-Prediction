from django.shortcuts import render
import pickle
import pandas as pd
import sklearn

model = pickle.load(open('pipeline.pkl', 'rb'))

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    new_entry = pd.DataFrame(
        {
        'brand': [str(request.GET['brand'])],
        'milage': [int(request.GET['milage'])],
        'accident': [str(request.GET['accident'])],
        'clean_title': [str(request.GET['clean_title'])],
        'interior_color': [str(request.GET['interior_color'])],
        'exterior_color': [str(request.GET['exterior_color'])],
        'tsm': [str(request.GET['tsm'])],
        'fuel': [str(request.GET['fuel'])],
        'Engine_Displacement': [float(request.GET['Engine_Displacement'])],
        'age': [int(request.GET['age'])]
        }
    )
    # Make prediction
    prediction = model.predict(new_entry)
    
    res = f'Your car price is: ${prediction[0]}'
    return render(request, 'result.html', {'prediction': res})
    
