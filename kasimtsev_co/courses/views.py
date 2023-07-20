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

    if not request.user.is_authenticated:
        return redirect (f"{reverse_lazy('login')}?next={reverse_lazy('course-enrole')}")

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

    return render (request, "payments/payment.html", {"confirmation_token": payment.confirmation.confirmation_token,})

def tableOfCourse (request):
    if not request.user.is_authenticated:
        return redirect (f"{reverse_lazy('login')}?next={reverse_lazy('course-enrole')}")

    if not services.getEnroleStatus(request.user):
        return redirect (f"course-enrole")
    
    return  render (request, "course-table.html")

def successEnroleView(request): 
    if not request.user.is_authenticated:
        return redirect (f"{reverse_lazy('login')}?next={reverse_lazy('course-enrole')}")

    if not services.getEnroleStatus (request.user): return redirect (reverse_lazy('course-enrole'))
    return render (request, "enrole-success.html")
        
def enroleLoginRequiredView(request):
    return render (request, "enrole-error.html")

def errorEnroleView(request):
    payment_id = request.session.get("payment_id")

    if payment_id:
        status = services.checkPaymentStatus (payment_id)
 
    return render (request, "enrole-error.html")
    
def aboutView (request):
    pass


def handler404(request, *args, **argv):
    return render ('404.html', {},)


def handler500(request, *args, **argv):
    return render ('500.html', {},)
