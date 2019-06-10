from django.shortcuts import render
from django.contrib import messages
from django.core.mail import EmailMessage

from .forms import CareerForm

def career_view(request):

	if request.method == 'POST':
		form = CareerForm(request.POST, request.FILES)
		if form.is_valid():
			subject='{} {} just name an application'.format(form.cleaned_data.get('firstname'), form.cleaned_data.get('lastname'))
			email = form.cleaned_data.get('email')
			message = form.cleaned_data.get('career_objective')
			attach = form.cleaned_data.get('cv')
			msg=EmailMessage(subject, message, email, ['info@assetplan.co.ke'])
			msg.attach(attach.name, attach.read(), attach.content_type)
			msg.send()

			form.save()


			messages.success(request, 'Your application was successfully!')
			form=CareerForm()
	else:
		form=CareerForm()

	context = {
		'form':form
	}


	return render(request, 'careers/career.html', context)