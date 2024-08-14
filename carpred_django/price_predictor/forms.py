from django import forms

class PredictionForm(forms.Form):
    brand = forms.CharField(label='brand')
    milage = forms.FloatField(label='milage')
    accident = forms.CharField(label='accident')
    clean_title = forms.CharField(label='clean_title')
    interior_color = forms.CharField(label='interior_color')
    exterior_color = forms.CharField(label='exterior_color')
    tsm = forms.CharField(label='tsm')
    fuel = forms.CharField(label='fuel')
    Engine_Displacement = forms.FloatField(label='Engine_Displacement')
    age = forms.FloatField(label='age')