from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from Noticias.forms import EscritorForm

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