from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField

#assign user model to a variable User
User = get_user_model()

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=100,blank=True)
    project_owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='project_owner')
    project_link = models.URLField(blank=True,max_length=200)
    description = models.TextField(blank=True)
    screenshot = CloudinaryField('image',blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.project_name)
class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,related_name='profile_user')
    profile_pic = models.ImageField(blank=True)
    bio = models.TextField(blank=True)
    contact = models.CharField(max_length=15)
    
    def __str__(self):
        return str(self.name.username)
class Rating(models.Model):
    design = models.IntegerField(blank=True)
    usability = models.IntegerField(blank=True)
    content = models.IntegerField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    rated_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='rater')
    project = models.ForeignKey(Project,on_delete=models.CASCADE,blank=True,related_name="project_rated")
    
    def __str__(self):
        return str(self.rated_by.username)


