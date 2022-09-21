from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUsers, UserProfile


class Gignupform(forms.ModelForm):
	
	class Meta:
		model= CustomUsers
		fields= ["username", "email", "Fullname", "Birth_date", "gender", "country"]

class CustomUserchangeform(UserChangeForm):
	class Meta(UserChangeForm.Meta):
		model= CustomUsers
		fields= ["username", "email"]


class UserProfileForm(forms.ModelForm):
	class Meta:
		model= UserProfile
		fields=[
			"profile_pic",
			"bio",
		]

class Signupform(forms.ModelForm):
	password=forms.PasswordInput()
	class Meta:
		model= CustomUsers
		fields= ["username", "email","Fullname", "Birth_date", "gender", "country", "password"]