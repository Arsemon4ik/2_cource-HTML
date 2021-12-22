from django.shortcuts import render,redirect
from django.views.generic import ListView,CreateView, TemplateView
from .models import Note
from django.utils.timezone import now

from django.http import HttpResponse
from django.views import View
from .tasks import complete_note

# Create your views here.
class NoteView(ListView):
    model = Note
    template_name = 'reminder/default.html'
    context_object_name = 'notes'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['notes'] = Note.objects.all()

    #     return context

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        date_finish = request.POST['date']
        text = request.POST['text']
        note = Note(name = name, text=text, date_finish = date_finish)
        note.save()

        complete_note.apply_async([note.id], countdown = 5)
        return redirect('/')


