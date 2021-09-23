from django.urls import path
from  . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard/', views.dashboard,name="dashboard"),
    path('rates/<int:pk>/', views.ratings,name="rates"),
    path('profile/', views.profile,name="profile"),
    path('bio/', views.bio,name="mybio"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)