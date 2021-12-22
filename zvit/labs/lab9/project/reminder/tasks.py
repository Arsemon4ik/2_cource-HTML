from celery import shared_task
from .models import Note

@shared_task
def complete_note(nid):
    order = Note.objects.get(pk = nid)
    order.complete = True
    order.save()