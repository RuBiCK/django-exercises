from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from tweets.models import Tweet
from django.http import Http404

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


