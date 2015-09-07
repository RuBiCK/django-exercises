from django.db import models

# Create your models here.
class User(models.Model):
    nick = models.CharField(max_length=20)
    join_date = models.DateTimeField('date created')
    email = models.EmailField(max_length=30,null=True)
    password = models.CharField(max_length=20,null=True,blank=False)
    error a mano #remove this line
    
class Tag(models.Model):
    titulo = models.CharField(max_length=50)
    def __str__(self):
        return self.titulo

class Tweet(models.Model):
    user = models.ForeignKey(User)
    tweet_text = models.CharField(max_length=140)
    pub_date = models.DateTimeField('date published')
    tags = models.ManyToManyField(Tag)


