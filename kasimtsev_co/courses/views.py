from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from . import services
from . import forms 

class mainPageView(CreateView):
    template_name = 'main-page.html'
    form_class = forms.UserQuestionsForm
    success_url = reverse_lazy('main-page')

    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        return result

class courseView(CreateView):
    template_name = 'course.html'
    form_class = forms.UserQuestionsForm
    success_url = reverse_lazy('course')

    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        return result

def courseEnroleView():
    payment = services.getPaymentConfirmation ()
    return redirect (payment.confirmation_url)

def succesEnroleView():
    pass
    #return render ()

    
def aboutView (request):
    pass


# Create your views here.
