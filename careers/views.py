from django.shortcuts import render

def career_view(request):
	return render(request, 'careers/career.html', {})