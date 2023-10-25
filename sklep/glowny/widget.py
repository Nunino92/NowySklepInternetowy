import requests
from django import forms
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

class WeatherWidget(forms.TextInput):
    def render(self, name, value, attrs=None, renderer=None):
        html = render_to_string('weather_widget.html', {'value': value})
        return mark_safe(html)

class WeatherWidgetForm(forms.Form):
    location = forms.CharField(label='Lokalizacja', max_length=100, required=True, widget=WeatherWidget())
