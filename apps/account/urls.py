from django.urls import path

from .views import (
    UserEmailRegisterView
)


app_name = 'account'


urlpatterns = [
    path('mail/', UserEmailRegisterView.as_view(), name='mail-register')
]