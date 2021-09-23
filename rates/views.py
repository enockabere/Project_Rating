from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from rateApp.models import Project, Profile, Rating

# Create your views here.
@login_required(login_url='accounts/login/')
def dashboard(request):
    project = Project.objects.all()
    
    #adding context
    ctx = {'project':project}
    return render(request,'main/dashboard.html', ctx)
@login_required(login_url='accounts/login/')
def ratings(request):
    return render(request,'main/rate.html')
@login_required(login_url='accounts/login/')
def profile(request):
    
    if request.method == 'POST':
        data = request.POST
        screenshot = request.FILES.get('image')
        
        dp = request.FILES.get('image')
        
        profile = Profile.objects.create(
            name = request.user,
            profile_pic = dp,
            bio = data['bio'],
            contact = data['contact']
        )
        
        project = Project.objects.create(
            project_name = data['p-name'],
            project_owner = request.user,
            project_link = data ['p-link'],
            description = data['description'],
            screenshot = screenshot,         
        )
        return redirect('profile')
    
    return render(request,'main/profile.html')