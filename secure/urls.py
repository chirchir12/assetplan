from django.urls import path
from .views import (
	index_view, 
	about_view, 
	contact_view,
	location_view
	)
app_name = 'security'
urlpatterns =[
	path('', index_view, name='index'),
	path('about/', about_view, name='about'),
	path('contact/', contact_view, name='contact'),
	path('location/', location_view, name='location')


]