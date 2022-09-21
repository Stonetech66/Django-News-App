from django import forms
from .models import Article, Comment, Category, Reply


class ArticleCreateform(forms.ModelForm):
	class Meta:
		model= Article
		fields= ["snippet", "title", "body", "Category", "header_image"]


class ReplyForm(forms.ModelForm):
	class Meta:
		model=Reply
		fields=[
			"body"
		]

	

	


class Createcomment(forms.ModelForm):
	
	class Meta:
		model= Comment
		fields= [ "comment"]


		


class ArticleUpdateform(forms.ModelForm):
	class Meta:
		model= Article
		fields= ["snippet", "title", "body", "Category"]
