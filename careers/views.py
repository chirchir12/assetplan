from django.shortcuts import render
from django.contrib import messages

from .forms import CareerForm

def career_view(request):

	if request.method == 'POST':
		form = CareerForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			messages.success(request, 'Your application was successfully!')
			form=CareerForm()
	else:
		form=CareerForm()

	context = {
		'form':form
	}


	return render(request, 'careers/career.html', context)