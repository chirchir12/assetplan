from django.shortcuts import render
from django.contrib import messages
from django.core.mail import EmailMessage

from .forms import QuoteForm

def property_protection_view(request):
	form = QuoteForm(request.POST)
	if form.is_valid():
		subject = '{}-{} made a quotation'.format(form.cleaned_data.get('fname'),form.cleaned_data.get('phone'))
		email = form.cleaned_data.get('email')
		message = form.cleaned_data.get('message')
		mail = EmailMessage(subject, message,email, ['info@assetplan.co.ke'] )
		mail.send()
		form.save()
		messages.success(request, 'Your request has been sent successfully.!!')
		form=QuoteForm()

	context = {
		'form':form
	}
	return render(request, 'services/propert_protection.html', context)



def personal_guard_protection_view(request):
	form = QuoteForm(request.POST)
	if form.is_valid():
		subject = '{}-{} made a quotation'.format(form.cleaned_data.get('fname'),form.cleaned_data.get('phone'))
		email = form.cleaned_data.get('email')
		message = form.cleaned_data.get('message')
		mail = EmailMessage(subject, message,email, ['info@assetplan.co.ke'] )
		mail.send()

		form.save()
		messages.success(request, 'Your request has been sent successfully.!!')
		form=QuoteForm()

	context = {
		'form':form}

	return render(request, 'services/personal_guard.html', context)

def event_security(request):
	form = QuoteForm(request.POST)
	if form.is_valid():
		subject = '{}-{} made a quotation'.format(form.cleaned_data.get('fname'),form.cleaned_data.get('phone'))
		email = form.cleaned_data.get('email')
		message = form.cleaned_data.get('message')
		mail = EmailMessage(subject, message,email, ['info@assetplan.co.ke'] )
		mail.send()

		form.save()
		messages.success(request, 'Your request has been sent successfully.!!')
		form=QuoteForm()

	context = {
		'form':form}
	return render(request, 'services/event_security.html', context)


def alarm_and_cctv_installation(request):
	form = QuoteForm(request.POST)
	if form.is_valid():
		subject = '{}-{} made a quotation'.format(form.cleaned_data.get('fname'),form.cleaned_data.get('phone'))
		email = form.cleaned_data.get('email')
		message = form.cleaned_data.get('message')
		mail = EmailMessage(subject, message,email, ['info@assetplan.co.ke'] )
		mail.send()

		form.save()
		messages.success(request, 'Your request has been sent successfully.!!')
		form=QuoteForm()

	context = {
		'form':form}
	return render(request, 'services/alarm_and_cctv_installation.html', context)


def security_audit(request):
	form = QuoteForm(request.POST)
	if form.is_valid():
		subject = '{}-{} made a quotation'.format(form.cleaned_data.get('fname'),form.cleaned_data.get('phone'))
		email = form.cleaned_data.get('email')
		message = form.cleaned_data.get('message')
		mail = EmailMessage(subject, message,email, ['info@assetplan.co.ke'] )
		mail.send()
		form.save()
		messages.success(request, 'Your request has been sent successfully.!!')
		form=QuoteForm()

	context = {
		'form':form}
	return render(request, 'services/security_audit.html', context)

def private_investigation(request):
	form = QuoteForm(request.POST)
	if form.is_valid():
		subject = '{}-{} made a quotation'.format(form.cleaned_data.get('fname'),form.cleaned_data.get('phone'))
		email = form.cleaned_data.get('email')
		message = form.cleaned_data.get('message')
		mail = EmailMessage(subject, message,email, ['info@assetplan.co.ke'] )
		mail.send()

		form.save()
		messages.success(request, 'Your request has been sent successfully.!!')
		form=QuoteForm()

	context = {
		'form':form}
	return render(request, 'services/private_investigation.html', context)

def dog_handling(request):
	form = QuoteForm(request.POST)
	if form.is_valid():
		subject = '{}-{} made a quotation'.format(form.cleaned_data.get('fname'),form.cleaned_data.get('phone'))
		email = form.cleaned_data.get('email')
		message = form.cleaned_data.get('message')
		mail = EmailMessage(subject, message,email, ['info@assetplan.co.ke'] )
		mail.send()
		
		form.save()
		messages.success(request, 'Your request has been sent successfully.!!')
		form=QuoteForm()

	context = {
		'form':form}
	return render(request, 'services/dog_handling.html', context)

