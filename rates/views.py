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
def ratings(request,pk):
    project = Project.objects.get(id=pk)
    ctx = {'project':project}
    #  project = Project.objects.create(
    #         project_name = data['p-name'],
    #         project_owner = request.user,
    #         project_link = data ['p-link'],
    #         project = request.get[id],
    #         screenshot = screenshot, 
                               
    #     )
    return render(request,'main/rate.html',ctx)
@login_required(login_url='accounts/login/')
def profile(request):
    
    if request.method == 'POST':
        data = request.POST
        screenshot = request.FILES.get('image')
                       
        project = Project.objects.create(
            project_name = data['p-name'],
            project_owner = request.user,
            project_link = data ['p-link'],
            description = data['description'],
            image = screenshot, 
                               
        )
        return redirect('profile')
    current = request.user.pk
    profile = Profile.objects.filter(name=current).all()
    print(profile)
    ctx={'profile':profile}
    return render(request,'main/profile.html',ctx)
@login_required(login_url='accounts/login/')
def bio(request):
    
    if request.method == 'POST':
        data = request.POST
        dp = request.FILES.get('dp')
                       
        bio = Profile.objects.create(
            bio = data['bio'],
            name = request.user,
            contact = data['contact'],
            image = dp, 
                               
        )
        return redirect('profile')
