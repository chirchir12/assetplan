from django.shortcuts import render
from .forms import ContactForm

def index_view(request):
	form = ContactForm(request.POST)
	
	if form.is_valid():
		form.save()
		form = ContactForm()

	context = {
		'form':form
		}
		
	return render(request, 'secure/index.html', context)


def about_view(request):
	form = ContactForm(request.POST)
	
	if form.is_valid():
		form.save()
		form = ContactForm()

	context = {
		'form':form
		}
	return render(request, 'secure/about.html', context)

def contact_view(request):
	return render(request, 'secure/contact.html', {})

def career_view(request):
	return render(request, 'secure/career.html', {})

def location_view(request):
	return render(request, 'secure/location.html', {})