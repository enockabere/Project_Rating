from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer,RegisterSerializer,LoginSerializer
from knox.models import AuthToken
from rest_framework.response import Response
User = get_user_model()
#register api class
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user':UserSerializer(user,context=self.get_serializer_context()).data,
            'token':AuthToken.objects.create(user)[1]
        })
        
#login api class
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self,request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            'user':UserSerializer(user,context=self.get_serializer_context()).data,
            'token':AuthToken.objects.create(user)[1]
        })
#get current user api