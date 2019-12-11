from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'alphatechblog/home.html', {})

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'alphatechblog/blog.html', {'blog':blogs})

def mentor(request):
    mentors = Mentor.objects.all()
    return render(request, 'alphatechblog/mentor.html', {'mentor':mentors})

def mentee(request):
    mentees = Mentee.object.all()
    return render(request, 'alphatechblog/mentee.html', {'mentee':mentees})

def author(request):
    return render(request, 'alphatechblog/author.html', {})


