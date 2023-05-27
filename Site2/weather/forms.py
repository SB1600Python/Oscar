from weather.models import City
from django.forms import ModelForm, TextInput


class CityForm(ModelForm):

    class Meta:
        model = City
        filter = ['name']
        widgets = {'name': TextInput(attrs={
            'class': 'form-control',
            'name': 'city',
            'placeholder': 'Напишить город',

        })}