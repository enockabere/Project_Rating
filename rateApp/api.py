from rest_framework import viewsets,permissions
from .serializers import ProjectSerializer
from  .models import Project

#todo viewsets
class ProjectViewset(viewsets.ModelViewSet):
    #specify queryset to take all model objects
    
    # queryset = Project.objects.all()
    
    permission_classes = [
        permissions.IsAuthenticated
    ]
    
    serializer_class = ProjectSerializer
    
    #method to return project of specific user
    def get_queryset(self):
        return self.request.user.project_owner.all()
    #submit project based on owner
    
    def perform_create(self,serializer):
        serializer.save(project_owner=self.request.user)