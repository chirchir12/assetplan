from django.shortcuts import render

def property_protection_view(request):
	return render(request, 'services/propert_protection.html', {})



def personal_guard_protection_view(request):
	return render(request, 'services/personal_guard.html', {})

def event_security(request):
	return render(request, 'services/event_security.html', {})


def alarm_and_cctv_installation(request):
	return render(request, 'services/alarm_and_cctv_installation.html', {})


def security_audit(request):
	return render(request, 'services/security_audit.html', {})

def private_investigation(request):
	return render(request, 'services/private_investigation.html', {})

def dog_handling(request):
	return render(request, 'services/dog_handling.html', {})

