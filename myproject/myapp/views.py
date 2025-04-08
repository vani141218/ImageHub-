from django.shortcuts import render, HttpResponse
from .forms import ImageForm
from .models import Image

# Create your views here.
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def index(request):
    img = Image.objects.all()
    
    return render(request, 'index.html', {'img':img})

def uploadImage(request):
    if request.method == "POST":
      form = ImageForm(request.POST, request.FILES)
      if form.is_valid():
       form.save()
    
    form = ImageForm()
    return render(request, 'upload.html', {'form':form})

