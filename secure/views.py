from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages

def index_view(request):
	form = ContactForm(request.POST)
	
	if form.is_valid():
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
		form.save()
		messages.success(request, 'Your message has been sent.!!')
		form = ContactForm()

	context = {
		'form':form
		}
	return render(request, 'secure/contact.html', context)

def location_view(request):
	return render(request, 'secure/location.html', {})
