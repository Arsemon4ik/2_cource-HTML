from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Note


# @receiver(post_save, sender=Notes)
# def notifyer(sender, instance, created, **kwargs):

#     if created: # если добавлена задача


