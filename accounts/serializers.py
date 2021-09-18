from rest_framework import serializers
from django.contrib.auth import get_user_model,authenticate

User = get_user_model()

#user serializer
class  UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ('id', 'username','email')
        
#register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('username','email', 'password','id')
        extra_kwargs = {"password":{"write_only":True}}
        
        def create(self,validated_data):
            user = User.objects.create_user(validated_data['username'],validated_data['email'],validated_data['password'])
            return user
#login serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password=serializers.CharField()
    
    def validate(self,attrs):
       user = authenticate(**attrs)
       
       #check if user authenticated
       if user and user.is_active:
           return user
       raise serializers.ValidationError("Incorrect Login credentials")
    