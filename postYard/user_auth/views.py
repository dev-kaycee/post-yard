from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages

from .forms import NewUserRegistrationForm


class RegisterView(View):
    def get(self, request):
        form = NewUserRegistrationForm()
        return render(request=request, template_name="register.html", context={"register_form":form})
    
    def post(self, request):
        form = NewUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home.html")
        print(form)
        messages.error(request, "Unsuccessfull. invalid details")
        # form = NewUserRegistrationForm()
        return render(request=request, template_name="register.html", context={"register_form":form})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # TODO user validation
        user_obj = authenticate(request, username=username, password=password) 

        if user_obj is not None:
            login(request, user_obj)
            user = request.user.username
            print(user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'login.html')