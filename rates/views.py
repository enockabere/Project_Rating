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

    rating = Rating.objects.filter(project=project)
    design = []
    usability=[]
    content = []
    if len(rating)> 0:
        for i in rating:
            design.append(i.design)
            usability.append(i.usability)
            content.append(i.content)
        design_avg= int((sum(design)/len(rating)*100)/10)
        usability_avg= int((sum(usability)/len(rating)*100)/10)
        content_avg= int((sum(content)/len(rating)*100)/10)
        
    
    else:
        design_avg = 0
        usability_avg = 0
        content_avg = 0
        
    
    ctx = {'project':project,"design":design_avg,"usability":usability_avg,"content":content_avg}
    if request.method == 'POST':
        data = request.POST
        rates = Rating.objects.create(
            design = data['design'],
            usability = data['usability'],
            content =data['content'],
            rated_by = request.user,
            project= project
        )
            
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
    project = Project.objects.filter(project_owner=current).all()
    ctx={'profile':profile,'project':project}
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
@login_required(login_url='accounts/login/')
def bio_update(request):
    
    if request.method == 'POST':
        data = request.POST
        dp = request.FILES.get('dps')
                       
        bio = Profile.objects.filter(name=request.user).update(
            bio = data['bios'],
            contact = data['contacts'],
            image = dp, 
                               
        )
        return redirect('profile')