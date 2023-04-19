from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Poets

@receiver(post_save, sender=User)
def create_poet(sender, instance, created, **kwargs):
    if created:
        poet = Poets.objects.create(user=instance, first_name=instance.first_name, last_name=instance.last_name)
        poet.save()

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.poets.save()