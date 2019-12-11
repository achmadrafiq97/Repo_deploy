from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog', views.blog, name='blog'),
    path('author', views.author, name='author'),
    path('mentee', views.mentee, name='mentee'),
    path('mentor', views.mentor, name='mentor')
]