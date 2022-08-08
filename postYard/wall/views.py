from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post
from django.views.generic.list import ListView
from django.contrib.auth import get_user_model


     
# class CreatePost(View): #TTODO add view to class name
#      def post(self, request):
#         user = UserView.getUser(request, 'secret')
#         request.data.update({'user':user.id})
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
 

# class GetPosts(APIView):
#     #get by FK
#     def get(self, request, id):
#         posts = Post.objects.filter(user_id=id).all()
#         serializer = PostSerializer(post, many=True)
#         return Response(serializer.data)
        
# Create your views here.

class HomeView(ListView):
    model = User
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        users = get_user_model().objects.all()
        context= {'users': users}
        return context


class UserView(ListView):
    model = Post
    template_name = 'user.html'

    # def get_context_data(self, **kwargs):
    #     context = self.kwargs
    #     print('ttttt',kwargs)
    #     userPosts = Post.objects.filter(user_id=4)
    #     context = {'user':User.username, 'posts': userPosts}
    #     return context
    def get_context_data(self):
        # qs = super(UserView, self).get_queryset()
        # p = qs.filter(post=self.kwargs.get('pk'))
        username = get_object_or_404(User, id=self.kwargs['user_id'])
        # username = User.objects.filter(id=user_id)
        all_posts_qs = Post.objects.filter(user_id=username).all()
        # context['post'] = all_posts_qs
        context = {'username': username, 'all_posts': all_posts_qs}
        print(context)
        return context



