from django.db import models
from datetime import datetime

# Create your models here.

class Poets(models.Model):
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    posts_count = models.IntegerField(default = 0)

class Post(models.Model):
    # user = models.CharField(Poets)
    title = models.CharField(max_length = 40, null = True)
    d_time = models.DateTimeField(default=datetime.now())
    data = models.TextField()
    poet_id = models.ForeignKey('Poets', on_delete=models.CASCADE, default=-1)