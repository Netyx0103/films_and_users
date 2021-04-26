from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Film(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    
    def __str__(self):
        return self.title

class Review(models.Model):
    master = models.ForeignKey(Film, on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    date_posted = models.DateTimeField(default = timezone.now)
    content = models.TextField()

    def __str__(self):
        return self.content

class Essay(models.Model):
    master = models.ForeignKey(Film, on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    date_posted = models.DateTimeField(default = timezone.now)
    content = models.TextField()

    def __str__(self):
        return self.content

class Comment(models.Model):
    film_master = models.ForeignKey(Film, on_delete = models.CASCADE)
    master = models.ForeignKey(Essay, on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    date_posted = models.DateTimeField(default = timezone.now)
    content = models.TextField()
    parent = models.ForeignKey('self', on_delete = models.CASCADE, null=True, related_name='child')

    def __str__(self):
        return self.content