from django.urls import path
from .views import (
	ArticleListview, 
	ArticleCreateview,
	ArticleDetailview,
	ArticleDeleteview, 
	ArticleUpdateview, 
	Commentdelete, 
	Category_Article,
	ReplyDelete, 
	ReplyListView,
	Searchview

	)

urlpatterns= [
	path('articles/', ArticleListview.as_view(), name= 'ArticleListview' ),
	path('articles/New', ArticleCreateview.as_view(), name= 'ArticleCreateview' ),
	path('articles/<int:pk>', ArticleDetailview.as_view(), name= 'ArticleDetailview' ),
	path('articles/<int:pk>/delete', ArticleDeleteview.as_view(), name= 'ArticleDeleteview' ),
	path('articles/<int:pk>/edit', ArticleUpdateview.as_view(), name= 'ArticleUpdateview' ),
	path('articles/comment/<int:pk>/delete', Commentdelete.as_view(), name= 'Commentdelete'),
	path('article/<slug:slug>/', Category_Article, name= 'category'),
	path('search/', Searchview.as_view(), name= 'search'),
	path('comment/<int:pk>/', ReplyListView.as_view(), name= 'comment-replies'),
	path('reply/<int:pk>/delete/', ReplyDelete.as_view(), name= 'reply-delete'),
	




]