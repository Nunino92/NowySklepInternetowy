from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

app_name = 'konto'

urlpatterns = [
    path('password_reset', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        success_url=reverse_lazy('konto:password_reset_done'),
    ), name='password_reset'),
    # Trasa do wyświetlania formularza resetowania hasła. Przyjmuje szablon 'password_reset.html' i przekierowuje na konto:password_reset_done po pomyślnym złożeniu formularza.

    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html',
    ), name='password_reset_done'),
    # Trasa do wyświetlania potwierdzenia wysłania wiadomości e-mail z linkiem resetowania hasła. Przyjmuje szablon 'password_reset_done.html'.

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_form.html',
        success_url=reverse_lazy('konto:password_reset_complete')
    ), name='password_reset_confirm'),
    # Trasa do resetowania hasła na podstawie linku w e-mailu. Przyjmuje parametry 'uidb64' i 'token' do weryfikacji żądania resetowania hasła.

    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'
    ), name='password_reset_complete'),
    # Trasa do wyświetlania potwierdzenia zresetowania hasła. Przyjmuje szablon 'password_reset_complete.html'.
]
