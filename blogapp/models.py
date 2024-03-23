from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date

class category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default='My blog')
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    # postdate=models.DateField(auto_now=True)
    postdate=models.DateTimeField(auto_now=True)
    category=models.CharField(max_length=255,default='noncategorized')
    image = models.ImageField(null=True,blank=True, upload_to="images/")

    def __str__(self):
        return self.title + '|'+str(self.author)

    def get_absolute_url(self):
        return reverse('home')

class comment(models.Model):
    post = models.ForeignKey(post,related_name ='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' %(self.post.title,self.name)



# Create your models here.