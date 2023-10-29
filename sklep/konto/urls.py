from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = 'konto'

urlpatterns = [
    path('password_reset', auth_views.PasswordResetView.as_view(template_name='password_reset.html',
                                                                success_url=reverse_lazy(
                                                                    'konto:password_reset_done'),
                                                                ), name='password_reset'),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'
                                                                         ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
