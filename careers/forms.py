from django import forms
from .models import Career


class CareerForm(forms.ModelForm):
	firstname        = forms.CharField(max_length=200, widget=forms.TextInput(
		attrs={

		}))
	lastname         = forms.CharField(max_length=250, widget=forms.TextInput(
		attrs={
		
		}))
	phone            = forms.CharField(max_length=100, widget=forms.TextInput(
		attrs={
		
		}))
	email            = forms.EmailField(max_length=255, widget=forms.EmailInput(
		attrs={
		
		}))
	location         = forms.CharField(max_length=255, widget=forms.TextInput(
		attrs={
		
		}))
	education        = forms.CharField(max_length=255, widget=forms.TextInput(
		attrs={
		
		}))
	cv               = forms.FileField(widget=forms.ClearableFileInput(
		attrs={
		
		}))
	career_objective = forms.CharField(widget=forms.Textarea(
		attrs={
		
		}))


	class Meta:
		model = Career 

		fields = ('firstname', 'lastname','phone', 'email','location', 'education', 'cv','career_objective')