from django.db import models

# Create your models here.

class Song(models.Model):
    name = models.TextField(max_length=100)
    duration = models.DurationField()
    upload_time = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class Podcast(models.Model):
    name = models.TextField(max_length=100)
    duration = models.DurationField()
    upload_time = models.DateTimeField(auto_now=True)
    host = models.TextField(max_length=100)
    participants = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Audiobook(models.Model):
    title = models.TextField(max_length=100)
    author = models.TextField(max_length=100)
    narrator = models.TextField(max_length=100)
    duration = models.DurationField()
    upload_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



