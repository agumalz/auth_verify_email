from django.urls import path
from .views import UserLogin,UserRegister,UserProfile, SendEmailVerification

urlpatterns = [
    path('register/',UserRegister.as_view(), name='register'),
    path('login/',UserLogin.as_view(), name='login'),
    path('profile/',UserProfile.as_view(), name='profile'),
    path('email_verification/',SendEmailVerification.as_view(), name='email_verification'),
]
