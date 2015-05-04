from django.forms import ModelForm
from Noticias.models import Escritor
class EscritorForm (ModelForm):
    class Meta:
        model = Escritor
        fields = ["nombre", "apellidos"]