from django.shortcuts import render, redirect
from .models import *
import cloudinary





# Create your views here.
def home(request):
  blogposts=Blogpost.objects.all().order_by('blogpost_date') #to view all blogposts available
  return render(request, 'home.html', {'blogposts':blogposts})

def about(request):
  return render(request, 'about.html')
  
def save_blogpost(request):
  if request.method=='POST':
    blog_title=request.POST['blog_title']
    blog_content=request.POST['blog_content']
    blog_image=request.FILES['blog_image']
    blog_image=cloudinary.uploader.upload(blog_image)
    blogpost=Blogpost(blog_title=blog_title, blog_content=blog_content, blog_image=blog_image)
    blogpost.save_blogpost()

    return redirect('/home', {'success': 'Blogpost Sucessfully Uploaded'})
  else:
    return render(request, 'home.html', {'danger': 'Blogpost Not Uploaded'})

    

def save_comment(request):
  if request.method=='POST':
    comment=request.POST['comment']
        