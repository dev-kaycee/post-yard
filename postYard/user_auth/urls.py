from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import LoginView, RegisterView, HomeView 

urlpatterns = [
    path('register', RegisterView.as_view(), name='perform_register'),
    path('register', RegisterView.as_view()),
    # path('login', LoginView.as_view(), name='login'),
    # path('login', LoginView.as_view(), name='perform_login'),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)