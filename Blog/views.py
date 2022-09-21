from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from .models import Article, Comment, Category, Reply
from .forms import Createcomment, ReplyForm
from django.urls import reverse_lazy, reverse
from .forms import ArticleCreateform, ArticleUpdateform
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.http import HttpResponse

# Create your views here.
class ArticleListview(ListView):
	model= Article
	template_name= 'ArticleListview.html'
	ordering= '-date_published'

	def get_context_data(self ,**kwargs):
		context= super().get_context_data(**kwargs)
		context["categoryy"]= Category.objects.all()
		return context

	def get_queryset(self):
		return Article.objects.all().select_related('Author').prefetch_related('Category')
def Category_Article(request, slug):
	j= Article.objects.select_related("Author").filter(Category__slug= slug)
	x=Article.objects.filter(Category__slug= slug).count()
	jj=slug.replace("-" ," ")
	k= {"category":j, "cats": jj, "count":x}

	return render(request, "Category_article.html", k)


 
class ArticleCreateview(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
	model= Article
	template_name= 'ArticleCreateview.html'
	form_class= ArticleCreateform
	login_url= 'account_login'
	permission_required= 'Blog.special_articlecreate'


	
	def form_valid(self, form):
		form.instance.Author= self.request.user
		
		return super().form_valid(form)

class ArticleDetailview(LoginRequiredMixin, DetailView):
	template_name= 'ArticleDetailView.html'
	model= Article
	login_url= 'account_login'


	def get_queryset(self):
		return Article.objects.all().select_related("Author").prefetch_related("comments")
	def get_context_data(self, **kwargs):
		context= super().get_context_data(**kwargs)
		context["comment_form"]= Createcomment()
		return context

	def post(self, request , *args, **kwargs):
		new_comment=Comment(Article= self.get_object(), comment= self.request.POST.get('comment'), name= self.request.user )
		new_comment.save()
		return self.get( self, request, *args, **kwargs)





class ArticleDeleteview(LoginRequiredMixin ,DeleteView):
	model= Article
	template_name= 'ArticleDelete.html'
	success_url= reverse_lazy('ArticleListview')
	login_url= 'account_login'
	


class ArticleUpdateview(LoginRequiredMixin, UpdateView):
	model= Article
	template_name= 'ArticleUpdateview.html'
	form_class= ArticleUpdateform
	login_url= 'account_login'


class Commentdelete(LoginRequiredMixin,DeleteView):
	model= Comment
	template_name= 'Commentdelete.html'
	login_url= 'account_login'
	
	def get_success_url(self):
		return reverse('ArticleDetailview', kwargs= {'pk': self.object.Article.pk })

class ReplyListView(LoginRequiredMixin , DetailView):
	model= Comment
	template_name="replies.html"
	login_url= "account_login"

	def get_queryset(self):
		return Reply.objects.all().select_related("name","Comment")

	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		context["reply_form"]= ReplyForm()
		return context

	def post(self, request, *args, **kwargs):
		new_reply=Reply.objects.create(name=self.request.user, Comment=self.get_object(), body=self.request.POST.get("body"))
		new_reply.save()
		return self.get(self, request, *args, *kwargs)


class ReplyDelete(LoginRequiredMixin ,DeleteView):
	model= Reply
	template_name= "Commentdelete.html"
	login_url= "account_login"
	
	def get_success_url(self):
		return reverse('comment-replies', kwargs={"pk":self.object.Comment.pk})
	



class Searchview(ListView):
	template_name= 'Search.html'
	model= Article

	def get_queryset(self):
		query= self.request.GET.get('q')
	
		return Article.objects.filter(Q(title__icontains= query)|Q(snippet__icontains= query) )
