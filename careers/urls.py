from django.urls import path 
from .views import career_view

app_name = 'careers'
urlpatterns = [
	path('', career_view, name='careers')
]