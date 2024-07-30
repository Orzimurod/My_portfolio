
from django.db import models


class PortfolioItem(models.Model):
    name =  models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/portfolio')
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/posts')
    body = models.TextField()


    def __str__(self):
        return self.title
    

class Education(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.title



