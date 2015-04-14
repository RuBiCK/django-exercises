from django.db import models

# Create your models here.
class User(models.Model):
    nick = models.CharField(max_length=20)
    join_date = models.DateTimeField('date created')
class Tweet(models.Model):
    user = models.ForeignKey(User)
    tweet_text = models.CharField(max_length=140)
    pub_date = models.DateTimeField('date published')