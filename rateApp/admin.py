from django.contrib import admin
from .models import Project, Profile, Ratings

# Register your models here.
admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Ratings)