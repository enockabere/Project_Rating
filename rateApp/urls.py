from rest_framework import routers
from .api import ProjectViewset

#create an instance of the router

router = routers.DefaultRouter()

router.register('/api/projects',ProjectViewset,'projects')

urlpatterns = router.urls