from django import forms
from .models import Career


class CareerForm(forms.ModelForm):
	firstname        = forms.CharField(max_length=200, widget=forms.TextInput(
		attrs={
		'class':'form-control form-control-sm mb-4'


		}))
	lastname         = forms.CharField(max_length=250, widget=forms.TextInput(
		attrs={
		'class':'form-control form-control-sm mb-4'
		
		}))
	phone            = forms.CharField(max_length=100, widget=forms.TextInput(
		attrs={
		'class':'form-control form-control-sm mb-4'
		
		}))
	email            = forms.EmailField(max_length=255, widget=forms.EmailInput(
		attrs={
		'class':'form-control form-control-sm mb-4'
		
		}))
	location         = forms.CharField(max_length=255, widget=forms.TextInput(
		attrs={
		'class':'form-control form-control-sm mb-4 has-error'
		
		}))
	education        = forms.CharField(max_length=255, widget=forms.TextInput(
		attrs={
		'class':'form-control form-control-sm mb-4 has-error'
		
		}))
	
	career_objective = forms.CharField(widget=forms.Textarea(
		attrs={
		'class':'form-control form-control-sm mb-4 has-error',
		'rows':3
		
		}))
	cv               = forms.FileField(widget=forms.ClearableFileInput(
		attrs={
		'class':'form-control-file mb-4 has-error'
		
		}))


	class Meta:
		model = Career 

		fields = ('firstname', 'lastname','phone', 'email','location', 'education', 'career_objective','cv')