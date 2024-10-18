from rest_framework import serializers
from .models import CustomUser, UserAddress, UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['no_hp','fcm_token']
        
class UserAdrressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ['address','city','postal_code','country','province']
        
class UserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(many=False, allow_null=True)
    user_address = UserAdrressSerializer(many=True, allow_null=True)
    class Meta:
        model = CustomUser
        fields = ['email','first_name','last_name','password','user_profile','user_address','is_email_verified']
        extra_kwargs = {'password':{'write_only' : True}}
        
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user