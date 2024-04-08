from django.shortcuts import render,redirect
from .models import profile
from django.views.generic import CreateView,ListView,DetailView,UpdateView

def createProfile(request):
    Profiles = profile.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        skill = request.POST.get('skill')


        Profile = profile(name=name,  age=age, address=address, skill=skill)
        Profile.save()

    return render(request, 'profile.html',{'profile':Profiles})

def listprofile(request):
    Profiles=profile.objects.all()

    return render(request,'listprofile.html',{'profile':Profiles})

def detailsview(request,profile_id):

    Profile=profile.objects.get(id=profile_id)
    return render(request,'detail.html',{'profile':profile})

def updateprofile(request,profile_id):

    Profile=profile_id.objects.get(id=profile_id)

    if request.method=="POST":

        name=request.POST.get('name')
        age=request.POST.get('age')
        address=request.POST.get('address')
        skill=request.POST.get('skill')

        profile.name=name
        profile.age=age
        profile.address=address
        profile.skill=skill

        profile.save()

        return redirect('/')

    return render(request,'update.html',{'profile':profile})

def deleteView(request,profile_id):

    Profile=profile.objects.get(id=profile_id)

    if request.method=="POST":

        profile.delete()

        return redirect('/')

    return render(request,'delete.html',{'profile':profile})