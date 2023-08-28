from django.db import models

# Create your models here.
from .extractdata import (
extract_text_from_pdf2,
extract_name,
extract_mobile_number,
extract_email,
extract_education,
extract_skills,)

class Post(models.Model):
	position=models.CharField(max_length=60)
	description=models.CharField(max_length=300)
	skills=models.CharField(max_length=200)
	vacant=models.BooleanField(default=False)
	experience=models.DecimalField(max_digits=3,decimal_places=2,default=0)
    



class MyModel(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(max_length=20,null=True, blank=True)
    skills = models.TextField()
    degree = models.CharField(max_length=100,null=True, blank=True)
    institute = models.CharField(max_length=100, null=True, blank=True)
    uploaded_file = models.FileField(upload_to='uploads/',null=True, blank=True)
    #extracted_text = models.TextField()  # Store the entire extracted text

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