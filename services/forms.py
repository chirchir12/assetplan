from django import forms 

from .models import Quote

class QuoteForm(forms.ModelForm):
	fname    = forms.CharField(max_length=250, help_text='enter your firstname', widget=forms.TextInput(
		attrs={
			'class':'form-control mb-4',
			'placeholder':'enter your firstname'

		}))
	lname    = forms.CharField(max_length=250, widget=forms.TextInput(
		attrs={
			'class':'form-control mb-4',
			'placeholder':'enter your lastname'
		}))
	phone    = forms.CharField(max_length=100, widget=forms.TextInput(
		attrs={
			'class':'form-control mb-4',
			'placeholder':'enter your phone number'

		
		}))
	email    = forms.EmailField(max_length=250, widget=forms.EmailInput(
		attrs={
			'class':'form-control mb-4',
			'placeholder':'enter your email'
		
		}))
	location = forms.CharField(max_length=200, widget=forms.TextInput(
		attrs={
			'class':'form-control mb-4',
			'placeholder':'Your Location'
		
		}))
	subject  = forms.CharField(max_length=255, widget=forms.TextInput(
		attrs={
			'class':'form-control mb-4',
			'placeholder':'Enter the type of  Service You Want'
		
		}))
	message  = forms.CharField(widget=forms.Textarea(
		attrs={
			'class':'form-control mb-4',
			'rows':4,
			'placeholder':'Give as a brief explanation'
		
		}))


	class Meta:
		model = Quote

		fields = ('fname','lname', 'phone', 'email','location','subject', 'message' )
