from django.conf.urls import patterns,url
from tweets import views

urlpatterns = patterns('',
                       url(r'^$',views.index, name='index'),
                       url(r'^(?P<nick>\w+)/$',views.user_tweets, name='user_tweets'),
                       url(r'^detail/(?P<tweet_id>\d+)/$',views.tweet_detail, name='tweet_detail'),
                       )
