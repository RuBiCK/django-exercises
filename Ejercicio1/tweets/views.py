from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from tweets.models import Tweet
def index(request):
    tweet_list = Tweet.objects.order_by('-pub_date')[:10]
    lista = []
    for tweet in tweet_list:
        lista.append(tweet.tweet_text + ' por ' + tweet.user.nick + '<br/>')
    output = ''.join(lista)
    return HttpResponse(output)

def user_tweets(request, nick):
    return HttpResponse('Este es el timeline de %s' % nick)

def tweet_detail(request, tweet_id):
    return HttpResponse('Este es el tweet con id %s' % tweet_id)