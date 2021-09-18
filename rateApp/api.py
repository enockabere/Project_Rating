from rest_framework import viewsets,permissions
from .serializers import ProjectSerializer
from  .models import Project

#todo viewsets
class ProjectViewset(viewsets.ModelViewSet):
    #specify queryset to take all model objects
    queryset = Project.objects.all()
    
    permission_classes = [
        permissions.AllowAny
    ]
    
    serializer_class = ProjectSerializer
    
    #method to return project of specific user
    
    #submit project based on owner