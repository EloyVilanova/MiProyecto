from django.shortcuts import render
from . import forms

# Create your views here.

def index(request): 
    return render(request, "home/index.html")

def crear_familiar(request):
    if request.method == "POST":
        form = forms.FamiliarForms(request.POST)
        if form.is_valid():
                form.save()
                return render(request, 'home/index.html')
    else: 
         form = forms.FamiliarForms()
         context = {'form' : form}
         return render(request, "home/crear-familiar.html", context)  
