from django import forms 

from .models import Quote

class QuoteForm(forms.ModelForm):
	fname    = forms.CharField(max_length=250, widget=forms.TextInput(
		attrs={

		}))
	lname    = forms.CharField(max_length=250, widget=forms.TextInput(
		attrs={
		
		}))
	phone    = forms.CharField(max_length=100, widget=forms.TextInput(
		attrs={
		
		}))
	email    = forms.EmailField(max_length=250, widget=forms.EmailInput(
		attrs={
		
		}))
	location = forms.CharField(max_length=200, widget=forms.TextInput(
		attrs={
		
		}))
	subject  = forms.CharField(max_length=255, widget=forms.TextInput(
		attrs={
		
		}))
	message  = forms.CharField(widget=forms.Textarea(
		attrs={
		
		}))


	class Meta:
		model = Quote

		fields = ('fname','lname', 'phone', 'email','location','subject', 'message' )
