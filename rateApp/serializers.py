from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    #create a meta class to define model
    class Meta:
        model = Project
        fields = ('project_name','project_owner','project_link','description','date_added')

    