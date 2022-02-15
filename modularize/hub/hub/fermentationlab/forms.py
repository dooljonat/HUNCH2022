from cProfile import label
from django import forms

model_dict = {
    '1': 'temperatures',
    '2':'humidities',
    '3':'co2_levels',
}
lookback_dict = {
    '1': '1',
    '2': '7',
    '3': '90',
    '4': '365',
}

class DownloadDataForm(forms.Form):
    MODEL_CHOICES = (
        ('1','Temperature'),
        ('2','Humidity'),
        ('3','CO2_Level'),
    )
    model_field = forms.ChoiceField(widget=forms.Select, choices=MODEL_CHOICES, label="Model:")

    LOOKBACK_OPTIONS = (
        ('1', '1'),
        ('2', '7'),
        ('3', '90'),
        ('4', '365'),
    )
    lookback_field = forms.ChoiceField(widget=forms.Select, choices=LOOKBACK_OPTIONS, label="Lookback Period:")