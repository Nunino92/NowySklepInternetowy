from django import forms
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

# Definicja niestandardowego widgeta do renderowania informacji o pogodzie
class WeatherWidget(forms.TextInput):
    def render(self, name, value, attrs=None, renderer=None):
        # Generowanie HTML na podstawie szablonu
        html = render_to_string('weather_widget.html', {'value': value})
        # Oznaczenie HTML jako bezpieczne
        return mark_safe(html)

# Formularz zawierający pole 'location' z niestandardowym widgetem
class WeatherWidgetForm(forms.Form):
    location = forms.CharField(label='Lokalizacja', max_length=100, required=True, widget=WeatherWidget())
