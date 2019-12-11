from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blog,Mentee,Mentor

# Create your views here.
def home(request):
    return render(request, 'alphatechblog/home.html', {})

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'alphatechblog/blog.html', {'blogs':blogs})

def mentor(request):
    mentors = Mentor.objects.all()
    return render(request, 'alphatechblog/mentor.html', {'mentors':mentors})

def mentee(request):
    mentees = Mentee.objects.all()
    return render(request, 'alphatechblog/mentee.html', {'mentees':mentees})

def author(request):
    return render(request, 'alphatechblog/author.html', {})

def form(request):
    return render(request, 'alphatechblog/form.html', {})

def konten_blog(request):
    input_blog = Blog(
        judul_blog = request.POST['Judul'],
        img_blog = request.POST['Foto'],
        paragraph_blog = request.POST['Isi Konten']
    )

    input_blog.save()
    return redirect('/blog')


