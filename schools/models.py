from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class School(models.Model):
    name = models.CharField(max_length=150)
    manager = models.CharField(max_length=150)
    location = models.CharField(max_length=264)
    city=models.CharField(max_length=20)
    Country = models.CharField(max_length=40)

    stage_choices =[
        ('Primary','Primary'),
        ('Preparatory','Preparatory'),
        ('Secondary','Secondary')
    ]
    stage = models.TextField(max_length=20 , choices= stage_choices)

    def __str__(self):
        return self.name

    def get_absolute_url(self): # i used this function to redirect after createschool
        return reverse('schools:detail',kwargs={'pk':self.pk})

class Student(models.Model):
    name =models.CharField(max_length=50)
    age = models.IntegerField()
    school = models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')
    
    def __str__(self):
        return self.name

    def get_absolute_url(self): # i used this function to redirect after create student
        return reverse('schools:std_detail',kwargs={'pk':self.pk}) #'sk':self.school.pk,
    