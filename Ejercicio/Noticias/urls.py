from django.conf.urls import patterns,url
from Noticias import views
urlpatterns = patterns('',
        url(r'^addescritorcbv/', views.AddEscritor.as_view()),
        url(r'^listaescritores/', views.EscritoresList.as_view()),
    )