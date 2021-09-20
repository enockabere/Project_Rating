from rest_framework import generics,permissions
from .serializers import UserSerializer,RegisterSerializer,LoginSerializer
from knox.models import AuthToken
from rest_framework.response import Response

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
        print(user)
        return Response({
            'user':UserSerializer(user,context=self.get_serializer_context()).data,
            'token':AuthToken.objects.create(user)[1]
        })
#get current user api
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user