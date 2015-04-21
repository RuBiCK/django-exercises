from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from tweets.models import Tweet
from django.http import Http404
from forms import RegisterForm

def index(request):
    latest_tweet_list = Tweet.objects.order_by('-pub_date')[:5]
    context = {'latest_tweet_list': latest_tweet_list}
    return render(request, 'tweets/index.html', context)

def user_tweets(request, nick):
    return HttpResponse('Este es el timeline de %s' % nick)

def tweet_detail(request, tweet_id):
    try:
        tweet = Tweet.objects.get(pk=tweet_id)
    except Tweet.DoesNotExist:
        raise Http404("El tweet no existe")
    context = {'tweet': tweet}
    return render(request, "tweets/detail.html", context)




def register (request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #TO-DO Genera el User a partir de los datos de cd
            return HttpResponseRedirect('/registro/welcome')
    else:
        form = RegisterForm()
    return render(request, 'registro.html', {'form': form})