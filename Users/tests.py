from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model

from Users.models import UserProfile
from .views import HomeView

# Create your tests here.

class UsersTest(TestCase):
	
	username= "Prince"
	email= "prince@gmail.com"
	def test_custom_user_create_user(self):
		customuser= get_user_model().objects.create_user(
				username= "Prince",
				email= "prince@gmail.com",
				gender="Male",
				country="Algeria")

		self.assertTrue(customuser.is_active)
		self.assertFalse(customuser.is_staff)
		self.assertFalse(customuser.is_superuser)	


	def test_Custom_super_user_create(self):
		Customsuperuser= get_user_model().objects.create_superuser(
		username="stone",
		email= "s@gmail.com",
		password= "qwerty1234"
			)
		self.assertTrue(Customsuperuser.is_active)
		self.assertTrue(Customsuperuser.is_staff)
		self.assertTrue(Customsuperuser.is_superuser)
		self.assertEqual(Customsuperuser.username, "stone")
		self.assertEqual(Customsuperuser.email, "s@gmail.com")




	def test_signup_form(self):
		resp= get_user_model().objects.create_user(self.username, self.email)
		self.assertEqual(get_user_model().objects.all()[0].username, "Prince")
		self.assertEqual(get_user_model().objects.all()[0].email, "prince@gmail.com")
		self.assertEqual(get_user_model().objects.all().count(), 1)



	def test_user_profile_detail_view(self):
		self.client.login(email= "s@gmail.com",password= "qwerty1234")
		resp= self.client.get(reverse("userprofile", args="1"))
		self.assertEqual(resp.status_code, 200)
		self.assertTemplateUsed(resp, "userprofile.html")
		self.assertContains(resp, "Bio")



	


class Homeviewtest(SimpleTestCase):

	def test_home_view(self):
		resp= self.client.get(reverse('home'))
		self.assertEqual(resp.status_code, 200)
		self.assertTemplateUsed(resp, "Home.html")

	def test_home_url_resolve(self):
		view= resolve('/')
		self.assertEqual(view.func.__name__, HomeView.as_view().__name__ )


