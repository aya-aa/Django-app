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
    #extracted_text = models.TextField()  # Store the entire extracted text
'''
    def save(self, *args, **kwargs):
        # Call your extraction functions here and update fields
        self.name = extract_name(self.uploaded_file.path)
        self.email = extract_email(self.uploaded_file.path)
        self.phone = extract_mobile_number(self.uploaded_file.path)
        self.skills = extract_skills(self.uploaded_file.path)
        #self.degree = extract_degree(self.uploaded_file.path)
        #self.institute = extract_institute(self.uploaded_file.path)
        #self.extracted_text = extract_all_text(self.uploaded_file.path)
        super().save(*args, **kwargs)
'''


from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django.db import models
from django.contrib.auth.models import User

class ModelSave(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    save_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Saved by {self.user} at {self.save_date}"

class UploadHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_date = models.DateTimeField(auto_now_add=True)
    # Link the UploadHistory model to the MyModel model (or the model you are using for saving data)
    saved_table = models.ForeignKey('MyModel', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('history_detail', args=[str(self.id)])
