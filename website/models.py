from django.db import models

from django.contrib.auth.models import User

# Create your models here.
from .extractdata import (
extract_text_from_pdf2,
extract_name,
extract_mobile_number,
extract_email,
extract_education,
extract_skills,)

class Post(models.Model):
    id = models.IntegerField(primary_key=True)  # Use the existing id field as primary key
    position=models.CharField(max_length=60)
    description=models.CharField(max_length=300)
    skills=models.CharField(max_length=200)
    vacant=models.BooleanField(default=False)
    experience=models.DecimalField(max_digits=3,decimal_places=2,default=0)
    



class MyModel(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    skills = models.TextField()
    degree = models.CharField(max_length=100,null=True, blank=True)
    institute = models.CharField(max_length=100, null=True, blank=True)
    uploaded_file = models.FileField(upload_to='uploads/',null=True, blank=True)



class MatchHistory(models.Model):
    position = models.ForeignKey(Post, on_delete=models.CASCADE)
    cv = models.ForeignKey(MyModel, on_delete=models.CASCADE)
    match_date = models.DateTimeField(auto_now_add=True)
