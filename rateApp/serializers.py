from rest_framework import serializers
from .models import Project,Profile,Rating

class ProjectSerializer(serializers.ModelSerializer):
    #create a meta class to define model
    class Meta:
        model = Project
        fields = ('project_name','project_owner','project_link','description','date_added')
class ProfileSerializer(serializers.ModelSerializer):
    #create a meta class to define model
    class Meta:
        model = Profile
        fields = ('name','bio','contact')
class RatingSerializer(serializers.ModelSerializer):
    #create a meta class to define model
    class Meta:
        model = Rating
        fields = ('design','usability','content','date','rated_by','project')
