from atexit import register
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import HomeView, UserView

urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
    path('user/<user_id>/', UserView.as_view(), name='viewUser'),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)