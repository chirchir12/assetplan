from django import forms 

from .models import Quote

class QuoteForm(forms.ModelForm):
	fname    = forms.CharField(max_length=250, help_text='enter your firstname', widget=forms.TextInput(
		attrs={
			'class':'form-control form-control-sm mb-2',
			'placeholder':'enter your name'

		}))
	phone    = forms.CharField(max_length=100, widget=forms.TextInput(
		attrs={
			'class':'form-control form-control-sm mb-2',
			'placeholder':'enter your phone number'

		
		}))
	email    = forms.EmailField(max_length=250, widget=forms.EmailInput(
		attrs={
			'class':'form-control form-control-sm mb-2',
			'placeholder':'enter your email'
		
		}))
	message  = forms.CharField(widget=forms.Textarea(
		attrs={
			'class':'form-control form-control-sm mb-2',
			'rows':2,
			'placeholder':'type your message here'
		
		}))


	class Meta:
		model = Quote

		fields = ('fname', 'phone', 'email', 'message' )
