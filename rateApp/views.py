from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Project,Profile,Rating
from .serializers import ProjectSerializer,RatingSerializer,ProfileSerializer
from .permissions import IsAuthenticatedOrReadOnly

from rest_framework import status
# Create your views here.

class  ProjectList(APIView):
    def get(self, request, formart=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)
    def post(self, request,formart=None):
        serializers = ProjectSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAuthenticatedOrReadOnly,)
class  ProfileList(APIView):
    def get(self, request, formart=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)
    def post(self, request,formart=None):
        serializers = ProfileSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAuthenticatedOrReadOnly,)
class  RatingList(APIView):
    def get(self, request, formart=None):
        all_rates = Rating.objects.all()
        serializers = RatingSerializer(all_rates, many=True)
        return Response(serializers.data)
    def post(self, request,formart=None):
        serializers = RatingSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAuthenticatedOrReadOnly,)