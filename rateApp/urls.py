from django.urls import path,include
from . import views

urlpatterns = [
    path('api/projects/', views.ProjectList.as_view()),
    path('api/projects/profile', views.ProfileList.as_view()),
    path('api/projects/ratings', views.RatingList.as_view()),
]