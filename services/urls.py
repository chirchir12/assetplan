from django.urls import path
from .views import (
	property_protection_view,
	personal_guard_protection_view,
	event_security,
	alarm_and_cctv_installation,
	security_audit,
	private_investigation,
	dog_handling
	)


app_name = 'services'
urlpatterns =[

	path('property-protection/',property_protection_view, name='property-protection' ),
	path('personal-guard/',personal_guard_protection_view, name='personal-guard' ),
	path('event-security/',event_security, name='event-security' ),
	path('dog-handling-and-patrols/',dog_handling, name='dog-handling' ),
	path('private-investigation/',private_investigation, name='private-investigation' ),
	path('security-audit/',security_audit, name='security-audit' ),
	path('alarm-and-cctv-installation/',alarm_and_cctv_installation, name='alarm-and-cctv-installation' ),


]