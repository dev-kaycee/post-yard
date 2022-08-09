from atexit import register
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import HomeView, UserView, PostCreateView
# from wall import views

app_name = 'wall'
urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
    path('user/<user_id>/', UserView.as_view(), name='viewUser'),
    path('newPost', PostCreateView.as_view(), name='newPost'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)