from django.urls import path
from . import views

app_name = 'alphatechblog'
urlpatterns = [
    path('', views.home, name='home'),
    path('blog', views.blog, name='blog'),
    path('author', views.author, name='author'),
    path('mentee', views.mentee, name='mentee'),
    path('mentor', views.mentor, name='mentor'),
    path('blog/form', views.form, name='form'),
    path('konten_blog', views.konten_blog, name='konten_blog')
]