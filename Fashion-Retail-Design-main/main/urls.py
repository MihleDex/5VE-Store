from django.urls import path

from main.forms import CustomAuthForm
from . import views
from .views import CustomLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('product', views.product, name='product'),
    path('home', views.index, name='index'),
    path('sign-up', views.signup, name='signup'),
    path('login/', CustomLoginView.as_view(authentication_form=CustomAuthForm), name='login'),

]