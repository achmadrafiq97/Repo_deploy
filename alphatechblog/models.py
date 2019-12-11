from django.db import models

# Create your models here.
class Blog(models.Model):
    img_blog = models.CharField(max_length=300)
    tanggal = models.CharField(max_length=20)
    comment = models.CharField(max_length=10)
    judul_blog = models.CharField(max_length=50)
    paragraph_blog = models.CharField(max_length=400)

    def __str__(self):
        return self.img_blog

class Mentor(models.Model):
    gambar_mentor = models.CharField(max_length=300)
    nama_mentor = models.CharField(max_length=30)
    experience = models.CharField(max_length=50)
    testimoni_mentor = models.CharField(max_length=300)

    def __str__(self):
        return self.nama_mentor


class Mentee(models.Model):
    gambar_mentee = models.CharField(max_length=300)
    nama_mentee = models.CharField(max_length=30)
    testimoni_mentee = models.CharField(max_length=300)

    def __str__(self):
        return self.nama_mentee
