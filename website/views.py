from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

#timporti el form eli amalteha
from .models import Post, MyModel

from .extractdata import (
extract_text_from_pdf2,
extract_name,
extract_mobile_number,
extract_email,
extract_education,
extract_skills,)
#timporti el function ta el test 



def posts(request):
	return render(request, 'posts.html', {'posts':Post.objects.all()})

def home(request):
	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In!")
			return redirect('home')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again...")
			return redirect('home')
	else:
		return render(request, 'home.html')




def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')








from django.views.generic.edit import FormView
from .forms import FileFieldForm


class FileFieldFormView(FormView):
    form_class = FileFieldForm
    template_name = "uploadform.html"
    success_url = "/upload/success/"

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        files = self.request.FILES.getlist('file_field')
        for f in files:
        	my_model_instance=MyModel(name=f.name,uploaded_file=f)

        	# Extract text from the PDF using your function
        	extracted_text = extract_text_from_pdf2(f)
        	name=extract_name(extracted_text)
        	number=extract_mobile_number(extracted_text)
        	email=extract_email(extracted_text)
        	education=extract_education(extracted_text)
        	skills=extract_skills(extracted_text)

            # Save the extracted information in the instance
        	my_model_instance.name = name
        	my_model_instance.email = email
        	my_model_instance.phone = phone
        	my_model_instance.skills = skills
        	my_model_instance.degree = degree
        	my_model_instance.institute = institute



        	my_model_instance.save()
            
        return super().form_valid(form)



def upload_success(request):
    return render(request, 'upload_success.html')