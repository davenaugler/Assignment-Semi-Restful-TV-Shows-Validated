from django.shortcuts import render,  redirect
from django.contrib import messages
from datetime import datetime
from .models import Shows

def index(request):  # GET
    return redirect("/shows")

def AddShowView(request):  # GET
    context = {
        'shows': Shows.objects.all()
    }
    return render(request, "srt_app/AddShow.html", context)

def AddShow(request):  # POST
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        print(request.POST)
        release_date = ('%m-%d-%Y')
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['release_date']
        description = request.POST['description']
        show = Shows.objects.create(title=title, network=network, release_date=release_date, description=description)
        return redirect(f'/shows/{show.id}')
        print("Diving into errors section")
        
def AllShows(request):  # GET
    context = {
        'shows': Shows.objects.all()
    }
    return render(request, "srt_app/DisplayShows.html", context)

def EditShowView(request, id):  # GET
    print(f"EditShow --> id: {id}")
    context = {
        'show': Shows.objects.get(id=id)
    }
    return render(request, "srt_app/EditShow.html", context)

def EditShow(request, id):  # POST
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['release_date']
        description = request.POST['description']
        show = Shows.objects.create(title=title, network=network, release_date=release_date, description=description)
        return redirect(f"/shows/{show.id}")

def ShowView(request, id):  # GET
    context = {
        'show': Shows.objects.get(id=id)
    }
    return render(request, "srt_app/OneShow.html", context)

def DeleteShow(request, id):  # POST
    show = Shows.objects.get(id=id)
    show.delete()
    return redirect(f"/shows")
