from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post
from django.views.generic.list import ListView
from django.views import View
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from .forms import CreatePost


class HomeView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        users = get_user_model().objects.all()
        post_count =[ len(Post.objects.filter(user_id=user).all()) for user in users]
        data = zip(users, post_count)
        context= {'data': data}
        return context


class UserView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'user.html'

    def get_context_data(self):
        username = get_object_or_404(User, id=self.kwargs['user_id'])
        all_posts_qs = Post.objects.filter(user_id=username).all()
        post_count = len(all_posts_qs)
        context = {'username': username,
        'all_posts': all_posts_qs,
        'post_count': post_count}
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['message']
    success_url = 'home'

    def form_valid(self, form):
        post_model = form.save(commit=False)
        post_model.user = self.request.user
        # app_model.user = User.objects.get(user=self.request.user) # Or explicit model 
        post_model.save()
        return HttpResponseRedirect('home')








