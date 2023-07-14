from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from . import forms 

class mainPageView(CreateView):
    template_name = 'main-page.html'
    form_class = forms.UserQuestionsForm
    success_url = reverse_lazy('main-page')

    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        return result

class coursesView(CreateView):
    pass
    
def aboutView (request):
    pass


# Create your views here.
