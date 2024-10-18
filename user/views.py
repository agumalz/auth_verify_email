from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer
from .forms import UserRegisterForm, UserLoginForm
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import CustomUser
from django.contrib import messages
from rest_framework.views import APIView
from utils.response_json import CostumResponJson
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


class UserRegister(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        form = UserRegisterForm(data=request.data)
        if form.is_valid():
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            user = CustomUser.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
            return CostumResponJson(statusCode=status.HTTP_200_OK, data=UserSerializer(user).data).generate_success_json()
            
        return CostumResponJson(statusCode=status.HTTP_400_BAD_REQUEST, data=form.errors).generate_error_json()
        
class UserLogin(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        form = UserLoginForm(data=request.data)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = CustomUser.objects.filter(email=email).first()
            if user is None or not user.check_password(password):
                return CostumResponJson(statusCode=status.HTTP_401_UNAUTHORIZED, data={'error':'invalid username or password'}).generate_error_json()
        
            refresh = RefreshToken.for_user(user)
            context = {
                'user' : UserSerializer(user).data,
                'accesss_token' : str(refresh.access_token),
                'refresh_token' : str(refresh),
            }
            return CostumResponJson(statusCode=status.HTTP_200_OK, data=context).generate_success_json()
        return CostumResponJson(form.errors, status=status.HTTP_400_BAD_REQUEST).generate_error_json()

class UserProfile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = CustomUser.objects.get(id=request.user.id)
        return CostumResponJson(statusCode=status.HTTP_200_OK, data=UserSerializer(user).data).generate_success_json()

class SendEmailVerification(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        
        context = {'email': request.user.email}
        html_message = render_to_string('send_email_verify.html', context)
        
        send_mail("Subject here","Here is the message","agumalzikhri@gmail.com",[request.user.email], fail_silently=False, html_message= html_message)
        
        
        return CostumResponJson(statusCode=status.HTTP_200_OK, data={'message': 'email verifikasi berhasil dikirim'}).generate_success_json()

# class EmailVerification(APIView):
    
#     def get(self, request):
 
       
