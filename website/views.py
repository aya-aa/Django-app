






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

import re


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

def preprocess_skills(skills):
    cleaned_skills = [skill.strip().lower() for skill in skills]
    cleaned_skills = [re.sub(r'\W+', ' ', skill) for skill in cleaned_skills]  # Remove non-alphanumeric characters
    return set(cleaned_skills)

class FileFieldFormView(FormView):
	form_class = FileFieldForm
	template_name = "uploadform.html"
	success_url = "success/"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['posts'] = Post.objects.all()
		return context

	def post(self, request, *args, **kwargs):
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def form_valid(self, form):
		files = self.request.FILES.getlist('file_field')
		selected_position_id = self.request.POST.get('selected_position')
		extracted_data_list=[]
		for f in files:
			my_model_instance=MyModel(name=f.name,uploaded_file=f)

        	# Extract text from the PDF using your function
			extracted_text = extract_text_from_pdf2(f)
			name=extract_name(extracted_text)
			number=extract_mobile_number(extracted_text)
			email=extract_email(extracted_text)
        	#education=extract_education(extracted_text)
			skills=extract_skills(extracted_text)




            # Save the extracted information in the instance
			my_model_instance.name = name
			my_model_instance.email = email
			my_model_instance.phone = number
			my_model_instance.skills = skills
        	#my_model_instance.degree = degree
        	#my_model_instance.institute = institute
			extracted_data = {
				'name': name,
				'number': number,
				'email': email,
				'skills': skills,
				}

			selected_position_id = self.request.POST.get('selected_position')
			selected_position = Post.objects.get(id=selected_position_id)



			lowercase_skills = preprocess_skills(skills)
			my_model_skills_lower = [skill.strip().lower() for skill in skills]
			selected_position_skills_lower = [skill.strip().lower() for skill in selected_position.skills.split(',')]


			print("Skills from MyModel instance:")
			print(my_model_skills_lower)

			print("Skills from selected_position:")
			print(selected_position_skills_lower)

			# Check for matching skills
			matching_skills = [skill for skill in my_model_skills_lower if skill in selected_position_skills_lower]




			# If there are matching skills, add the extracted data to the list
			if matching_skills:
				extracted_data_list.append(extracted_data)
			print("Matching skills (lowercase):")
			print(matching_skills)


        	#my_model_instance = MyModel(name=name, email=email, phone=number, skills=skills)
        	# Save the extracted information in the instance
			my_model_instance.name = name
			my_model_instance.email = email
			my_model_instance.phone = number
			my_model_instance.skills = skills
			my_model_instance.save()

			

		posts = Post.objects.all()




		position= selected_position.position
		context = {
		'form': form,
		'extracted_data': extracted_data_list,
		'posts': posts,
		'position_id': selected_position_id,
		'position':position,
		}
		return render(self.request, 'success.html', context)
            
 



def upload_success(request):
    return render(request, 'success.html')







