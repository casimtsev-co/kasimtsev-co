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

def courseEnroleView(request):
    print ("courseEnroleView")

    if not request.user.is_authenticated:
        return redirect (f"{reverse_lazy('login')}?next={request.path}")

    payment_id = request.session.get("payment_id")

    if payment_id:
        status = services.checkPaymentStatus (payment_id)
        if status == "succeeded":
            services.enroleUser (request.user)
            return redirect ("enrole-success")

        if status != "pending":
            return redirect ("enrole-error")

    payment = services.getPaymentConfirmation ()
    request.session["payment_id"] = payment.id

    return render (request, "payments/payment.html", {"confirmation_token": payment.confirmation.confirmation_token, "return_url": request.build_absolute_uri(reverse_lazy('course-enrole'))})

def successEnroleView(request): 
    print ("successEnroleView")
    return render (request, "enrole-success.html", context = {"login-required": True})
        
def enroleLoginRequiredView(request):
    return render (request, "enrole-error.html", context = {"login-required": True})

def errorEnroleView(request):
    payment_id = request.session.get("payment_id")

    if payment_id:
        status = services.checkPaymentStatus (payment_id)
        print (status)
 
    return render (request, "enrole-error.html")
    
def aboutView (request):
    pass

