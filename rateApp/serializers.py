from rest_framework import serializers
from .models import Project, Profile, User, Rating

class ProjectSerializer(serializers.ModelSerializer):
    #create a meta class to define model
    class Meta:
        model = Project
        fields = '_all_'
    class Meta:
        model = Profile
        fields = '_all_'
    class Meta:
        model = Rating
        fields = '_all_'