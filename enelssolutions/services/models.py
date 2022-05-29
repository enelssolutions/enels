from django.db import models

# Create your models here.
class Subscriber(models.Model):
    name = models.CharField(max_length=264)
    email = models.EmailField(max_length=264)

    def __str__(self):
        return self.name

class Contact(models.Model):
    firstname = models.CharField(max_length=264)
    lastname = models.CharField(max_length=264)
    email = models.CharField(max_length=264)
    subject = models.CharField(max_length=264)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.subject
