from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .views import CustomLoginView, PasswordsChangeView

app_name = 'glowny'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/',  CustomLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('settings/', views.update, name='update'),
    path('password/', PasswordsChangeView.as_view(template_name='update_password.html'), name='update_password'),
    path('weather/', views.weather_widget, name='weather_widget'),

]