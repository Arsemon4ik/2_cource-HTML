from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class BaseRegisterView(LoginRequiredMixin,TemplateView):
    template_name = 'sign/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_user'] = not self.request.user.groups.filter(name = 'common').exists()
        return context
