from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible

# Create your models here.

@deconstructible
class PoetProfilePicPath:
    def __init__(self, subdirectory):
        self.subdirectory = subdirectory

    def __call__(self, instance, filename):

        first_name = instance.first_name
        last_name = instance.last_name


        file_path = f'static/{self.subdirectory}/{first_name}-{last_name}.jpg'

        return file_path


class Poets(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    posts_count = models.IntegerField(default = 0)
    pfp = models.ImageField(default = 'default.jpg', upload_to = PoetProfilePicPath('pfps'))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Post(models.Model):
    title = models.CharField(max_length = 40, null = True)
    d_time = models.DateTimeField(default=datetime.now())
    data = models.TextField()
    poet_id = models.ForeignKey('Poets', on_delete=models.CASCADE, default=-1)

    def __str__(self):
        return f"{self.id}: {self.title}"


class Queries(models.Model):
    name = models.CharField(max_length = 40)
    email = models.EmailField(max_length = 50)
    msg = models.TextField(null = False)

    def __str__(self):
        return f"{self.name}: {self.email}"