from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import ContactForm
from django.contrib import messages

def index_view(request):
	form = ContactForm(request.POST)
	
	if form.is_valid():
		subject = '{}-{} made an inquiry'.format(form.cleaned_data.get('fullname'),form.cleaned_data.get('phone'))
		email   = form.cleaned_data.get('email')
		message = form.cleaned_data.get('message')
		mail = EmailMessage(subject, message, email, ['info@assetplan.co.ke'])
		mail.send()
		form.save()
		messages.success(request, 'Your message has been sent.!!')
		form = ContactForm()

	context = {
		'form':form
		}
		
	return render(request, 'secure/index.html', context)


def about_view(request):
	form = ContactForm(request.POST)
	
	if form.is_valid():
		subject = '{}-{} made an inquiry'.format(form.cleaned_data.get('fullname'),form.cleaned_data.get('phone'))
		email   = form.cleaned_data.get('email')
		message = form.cleaned_data.get('message')
		mail = EmailMessage(subject, message, email, ['info@assetplan.co.ke'])
		mail.send()
		form.save()
		messages.success(request, 'Your message has been sent.!!')
		form = ContactForm()

	context = {
		'form':form
		}
	return render(request, 'secure/about.html', context)

def contact_view(request):
	form = ContactForm(request.POST)
	
	if form.is_valid():
		subject = '{}-{} made an inquiry'.format(form.cleaned_data.get('fullname'),form.cleaned_data.get('phone'))
		email   = form.cleaned_data.get('email')
		message = form.cleaned_data.get('message')
		mail = EmailMessage(subject, message, email, ['info@assetplan.co.ke'])
		mail.send()
		form.save()
		messages.success(request, 'Your message has been sent.!!')
		form = ContactForm()

	context = {
		'form':form
		}
	return render(request, 'secure/contact.html', context)

def location_view(request):
	return render(request, 'secure/location.html', {})
