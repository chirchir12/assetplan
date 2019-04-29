from django.shortcuts import render
from .forms import CareerForm

def career_view(request):

	if request.method == 'POST':
		form = CareerForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
	else:
		form=CareerForm()

	context = {
		'form':form
	}


	return render(request, 'careers/career.html', context)