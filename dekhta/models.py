from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Poets(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    posts_count = models.IntegerField(default = 0)
    pfp = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Post(models.Model):
    # user = models.CharField(Poets)
    title = models.CharField(max_length = 40, null = True)
    d_time = models.DateTimeField(default=datetime.now())
    data = models.TextField()
    poet_id = models.ForeignKey('Poets', on_delete=models.CASCADE, default=-1)