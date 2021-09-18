from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,related_name='profile_user')
    projects = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='projects')
    profile_pic = models.ImageField(blank=True)
    bio = models.TextField(blank=True)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return str(self.name.username)
class Ratings(models.Model):
    design = models.IntegerField(blank=True,max_length=2)
    usability = models.IntegerField(blank=True,max_length=2)
    content = models.IntegerField(blank=True,max_length=2)
    date = models.DateTimeField(auto_now_add=True)
    rated_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='rater')
    
    def __str__(self):
        return str(self.rated_by.username)
