
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
    # created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title
    

class Education(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.title


class Experience(models.Model):
    position_name = models.CharField(max_length=255)  
    company_name = models.CharField(max_length=255)  
    working_period = models.CharField(max_length=100)  
    tasks = models.TextField()                       
    skills = models.TextField()                     

    def __str__(self):
        return f"{self.position_name} at {self.company_name}"


