from rest_framework import routers
from .api import ProjectViewset

from django.conf import settings
from django.conf.urls.static import static
#create an instance of the router

router = routers.DefaultRouter()

router.register('api/projects',ProjectViewset,'projects')

urlpatterns = router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)