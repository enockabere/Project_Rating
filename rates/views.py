from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='accounts/login/')
def dashboard(request):
    return render(request,'main/dashboard.html')
@login_required(login_url='accounts/login/')
def ratings(request):
    return render(request,'main/rate.html')
@login_required(login_url='accounts/login/')
def profile(request):
    return render(request,'main/profile.html')