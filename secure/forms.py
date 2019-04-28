from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
	fullname = forms.CharField(label='', widget=forms.TextInput(
		attrs={
		'class':'form-control',
		'placeholder':'Fullname'
		}
		))
	email    = forms.EmailField(label='', widget=forms.EmailInput(
		attrs={
		'class':'form-control',
		'placeholder':'Email'
		}
		))
	phone    = forms.CharField(label='', widget=forms.TextInput(
		attrs={
		'class':'form-control',
		'placeholder':'Phone Number'
		}
		))
	message  = forms.CharField(label="" ,widget=forms.Textarea(
		attrs={
		'class':'form-control chirchir',
		'placeholder':'Message',
		'rows':4,
		'cols':50
		
		}))

	class Meta:
		model = Contact
		fields = ('fullname', 'email', 'phone', 'message')


	
