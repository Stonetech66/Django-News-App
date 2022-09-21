from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUsers, UserProfile
from .forms import Signupform
from django.contrib.auth import authenticate, login
from django.db  import transaction

from Blog.models import Article
from .forms import Gignupform, UserProfileForm
from django.urls import reverse_lazy
# Create your views here.



class HomeView(TemplateView):
	template_name= "Home.html"




class EditAccountInformation(LoginRequiredMixin,UpdateView):
	model= CustomUsers
	template_name="Accountinfo_edit.html"
	fields= [ "username", "email", "gender", "Birth_date", "country"]


class AccountInformation(LoginRequiredMixin,DetailView):
	model= CustomUsers
	template_name= "AccountInformation.html"
	




class UserEditProfile(LoginRequiredMixin,UpdateView):
	model= UserProfile
	template_name= "userprofileedit.html"
	form_class= UserProfileForm
	login_url= "account_login"
	

class UserProfile(LoginRequiredMixin,DetailView):
	model= UserProfile
	template_name= "userprofile.html"
	context_object_name= "user"
	
	


"""
@transaction.atomic
def signupform(request):
	form= Signupform(request.POST)
	if form.is_valid():
		username=form.cleaned_data["username"]
		email=form.cleaned_data["email"]
		country=form.cleaned_data["country"]
		Fullname=form.cleaned_data["Fullname"]
		gender=form.cleaned_data["gender"]
		password=form.cleaned_data["password"]
		user=CustomUsers.objects.create(username=username, email=email, country=country, Fullname=Fullname,gender=gender,)
		user.set_password(password)
		user.save()
		
	
	return render(request, "signup.html", {"context":form})

"""