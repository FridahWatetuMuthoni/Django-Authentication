from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Profile

#sender
User = get_user_model()

"""
post_save is fired up after the models is connected to is saved .
We want to create a profile everytime a User is created 
@reciever(signal, sender)
(sender, instance, created, **kwargs)=>this arguements come from post_save signal
"""

#Reciever
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#saving the profile        
@receiver(post_save, sender=User)
def save_profile(sender, instance,**kwargs):
    instance.profile.save()
