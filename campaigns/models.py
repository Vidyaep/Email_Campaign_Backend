from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Campaign(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    recipients = models.ManyToManyField(User, related_name='campaigns')
    scheduled_time = models.DateTimeField()
    status = models.CharField(max_length=50, default='Scheduled')  

    def __str__(self):
        return self.name
