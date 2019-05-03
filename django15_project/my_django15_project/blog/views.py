from django.shortcuts import render,redirect
from .models import *
from .forms import *


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def addasseth(request):
    if request.method == "POST":
        form = addassetForm(request.POST)
        if form.is_valid():
            blog_item = form.save(commit=False)
            blog_item.save()
            return redirect('/blog/addasseth/')
    else:
        form = addassetForm()
    return render(request, 'blog/AddAsset.html', {'form': form})

def ProjectDetailh(request):
    if request.method == "POST":
        form = addProjectDetailform(request.POST)
        if form.is_valid():
            blog_item = form.save(commit=False)
            blog_item.save()
            return redirect('/blog/addasseth/')
    else:
        form = addProjectDetailform()
    return render(request, 'blog/projectdetail.html', {'form': form})

def AddProjectDocumenth(request):
    if request.method == "POST":
        form = AddProjectDocumentForm(request.POST,request.FILES)
        if form.is_valid():
            blog_item = form.save(commit=False)
            blog_item.save()
            return redirect('/blog/AddProjectDocumenth/')
    else:
        form = AddProjectDocumentForm()
    return render(request, 'blog/projectdocument.html', {'form': form})
