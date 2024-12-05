from django import forms

class EconomicImpactForm(forms.Form):
    age = forms.FloatField(label="Age")
    gender = forms.CharField(label="Gender")


class AdaptationPredictionForm(forms.Form):
    total_education_facilities = forms.FloatField(label="total education facilities")
    escapee_rate = forms.FloatField(label="escapee rate")
    mental_illness_rate = forms.FloatField(label="mental illness rate")

class CrimePredictionForm(forms.Form):
    state = forms.CharField(label="state ")
    crime_type = forms.CharField(label="crime type ")

