from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from Noticias.forms import *
from Noticias.models import *
from django.views.generic import ListView
from django.db.models import Count
class AddEscritor (View):
    def get (self, request):
        form = EscritorForm()
        return render (request, 'add_escritor.html', {'form':form})
    def post(self, request):
        form = EscritorForm (request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            form.save()
           #TODO return HttpResponseRedirect ("/noticias/welcome")
            return HttpResponse('<p class="bg-success">Usuario registrado!</p>')
        return render (request, 'add_escritor.html', {'form':form})

class EscritoresList(ListView):
    model = Escritor
    template_name = 'escritores_list.html'

    def get_context_data(self, **kwargs):
        context = super(EscritoresList, self).get_context_data(**kwargs)
        noticias = Noticia.objects.values('autor').annotate(dcount=Count('autor'))
        noticias_bien = {}
        for elemento in noticias:
            noticias_bien[elemento["autor"]] = elemento["dcount"]
            context["noticias"] = noticias_bien
            return context
