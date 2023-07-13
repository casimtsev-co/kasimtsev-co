from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .forms import UserSignupForm

def StudentRegistrationView(request):
    form = UserSignupForm()
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Регистрация успешна." )
            return redirect('main-page')
        messages.error(request, "Ошибка при регистрации.")
    return render (request=request, template_name = 'registration/signup.html', context={"form":form})

class StudentRegistrationView_old(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserSignupForm
    success_url = reverse_lazy('main-page')
    def form_valid(self, form):

        result = super().form_valid(form)
        print(result)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'],
                            password=cd['password1'])
        login(self.request)
        return result


# Create your views here.


