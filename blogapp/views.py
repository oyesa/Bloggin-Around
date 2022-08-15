from django.shortcuts import render, redirect
from .models import *
import cloudinary





# Create your views here.
def home(request):
  return render(request, 'home.html')


def save_blogpost(request):
  if request.method=='POST':
    blog_title=request.POST['blog_title']
    

    