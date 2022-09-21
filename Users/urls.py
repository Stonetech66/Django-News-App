from django.urls import path
from . import views 
urlpatterns= [
    path("<int:pk>/", views.AccountInformation.as_view(), name= 'users-profile'),
    path("<int:pk>/edit-account/", views.EditAccountInformation.as_view(), name= "edit-Account"),
    path("<int:pk>/edit-profile/", views.UserEditProfile.as_view(), name= "userprofile-edit"),
    path("<int:pk>/user-profile/", views.UserProfile.as_view(), name= "userprofile"),
    ] 