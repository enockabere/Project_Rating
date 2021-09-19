from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer,RegisterSerializer
from rest_framework.response import Response
User = get_user_model()
#register api class
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response((
            'user',
            'token'
        ))
        
#login api class
#get current user api