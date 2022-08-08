from django.shortcuts import render, redirect
from django.views import View
# from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages

from .forms import NewUserRegistrationForm

# Create your views here.
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